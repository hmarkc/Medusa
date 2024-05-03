import json
import sys
import pandas as pd
import os
import argparse

def get_throughput_results(input_file):
    with open(input_file, "r") as f:
        data = [json.loads(line) for line in f]

    new_tokens = []
    wall_time = []
    throughputs = []
    accept_lengths = []
    idxs = []
    for d in data:
        for choice in d["choices"]:
            new_tokens.extend(choice["new_tokens"])
            wall_time.extend(choice["wall_time"])
            for i in range(len(choice["new_tokens"])):
                throughputs.append(choice["new_tokens"][i] / choice["wall_time"][i])
                accept_lengths.append(choice["new_tokens"][i] / (choice["idxs"][i]+1))
            idxs.extend([idx+1 for idx in choice["idxs"]])
            
    return sum(new_tokens) / sum(wall_time), sum(throughputs) / len(throughputs), sum(new_tokens) / sum(idxs), sum(wall_time) / sum(idxs)


def get_tree_latency(input_file):
    with open(input_file, "r") as f:
        data = [json.loads(line) for line in f]

    latencies = {}
    for d in data:
        latencies[d['tree_length']] = sum(d['choices'][0]['wall_time'])
            
    return latencies


def print_average_throughputs(input_files):
    throughputs1, throughputs2, accepth_lengths, forward_pass_time = list(zip(*[get_throughput_results(input_file) for input_file in input_files]))
    print(f"Macro-Average throughput: {sum(throughputs1) / len(throughputs1):.3f} tokens/s")
    print(f"std: {pd.Series(throughputs1).std():.3f}")
    print(f"Micro-Average throughput: {sum(throughputs2) / len(throughputs2):.3f} tokens/s")
    print(f"std: {pd.Series(throughputs2).std():.3f}")
    print(f"Average accept lengths: {sum(accepth_lengths) / len(accepth_lengths):.5f}")
    print(f"std: {pd.Series(accepth_lengths).std():.5f}")
    print(f"Average forward pass time: {sum(forward_pass_time) / len(forward_pass_time):.5f} s")
    print(f"std: {pd.Series(forward_pass_time).std():.5f}")
    
    return (sum(accepth_lengths) / len(accepth_lengths)) / (sum(forward_pass_time) / len(forward_pass_time))


def parse_file_name(file_name):
    # file name is in the format prefix{ddd}_0.json or prefix{dd}_1.json or prefix{d}_2.json where d is a digit
    prefix = file_name.split("_")[-2]
    rst = 0
    for i in range(1, 4):
        if prefix[-i:].isdigit():
            rst = prefix[-i:]
    return int(rst)
    

def main(args):
    input_files = args.input_files
    # if the input is a directory, iterate over all files in the directory
    if os.path.isdir(input_files[0]):
        input_files = [os.path.join(input_files[0], f) for f in os.listdir(input_files[0]) if 'tree_latency.jsonl' not in f]
        # group files by prefix. Assume that the files are named as prefix1_0.json, prefix1_1.json, prefix2_0.json, prefix2_1.json, etc. The resulting list should be prefix0_0.json, prefix0_1.json, prefix0_2.json, prefix1_0.json, prefix1_1.json, etc.
        input_files = sorted(input_files, key=lambda x: parse_file_name(x))
        # for each group, get the average throughput using print_average_throughputs
        max_accepth_lenght_to_forward_pass_time = 0
        best_tree = None
        for i in range(0, len(input_files), args.n):
            # print prefix
            print(">>>", input_files[i].split("_")[-2])
            ratio = print_average_throughputs(input_files[i:i+args.n])
            if ratio > max_accepth_lenght_to_forward_pass_time:
                max_accepth_lenght_to_forward_pass_time = ratio
                best_tree = input_files[i].split("_")[-2]
        print(f"Best sparse tree: {best_tree}, ratio: {max_accepth_lenght_to_forward_pass_time}")
    elif 'tree_latency.jsonl' in input_files[0]:
        latencies = get_tree_latency(input_files[0])
        input_files = [os.path.join(input_files[1], f) for f in os.listdir(input_files[1]) if 'tree_latency.jsonl' not in f]
        input_files = sorted(input_files, key=lambda x: parse_file_name(x))
        # for each group, get the average throughput using print_average_throughputs
        max_accepth_lenght_to_forward_pass_time = 0
        best_tree = None
        for i in range(0, len(input_files), 1):
            # print prefix
            print(">>>", input_files[i].split("_")[-2])
            tree_length = parse_file_name(input_files[i])
            if tree_length not in latencies:
                continue
            _, _, accepth_lengths, _ = get_throughput_results(input_files[i])
            ratio = accepth_lengths / latencies[tree_length]
            if ratio > max_accepth_lenght_to_forward_pass_time:
                max_accepth_lenght_to_forward_pass_time = ratio
                best_tree = input_files[i].split("_")[-2]
            print("Ratio: ", ratio, 'Accept length: ', accepth_lengths, 'Latency: ', latencies[tree_length])
        print(f"Best sparse tree: {best_tree}, ratio: {max_accepth_lenght_to_forward_pass_time}")
    else: 
        print_average_throughputs(input_files)


if __name__ == "__main__":
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("input_files", nargs="+", help="Input files to get throughput results")
    parser.add_argument("--n", type=int, default=1, help="Number of files to group")
    args = parser.parse_args()
    main(args)