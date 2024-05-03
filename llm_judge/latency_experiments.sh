# baseline 7b
python gen_model_answer_baseline.py  --model-path FasterDecoding/medusa-vicuna-7b-v1.3 --model-id medusa-vicuna-7b-v1.3-0  --answer-file data/mt_bench/experiments/vicuna-7b-baseline0.jsonl
python gen_model_answer_baseline.py  --model-path FasterDecoding/medusa-vicuna-7b-v1.3 --model-id medusa-vicuna-7b-v1.3-0 --answer-file data/mt_bench/experiments/vicuna-7b-baseline1.jsonl
python gen_model_answer_baseline.py  --model-path FasterDecoding/medusa-vicuna-7b-v1.3 --model-id medusa-vicuna-7b-v1.3-0 --answer-file data/mt_bench/experiments/vicuna-7b-baseline2.jsonl

# medusa 7b
python gen_model_answer_medusa.py  --model-path FasterDecoding/medusa-vicuna-7b-v1.3 --model-id medusa-vicuna-7b-v1.3-0  --answer-file data/mt_bench/experiments/vicuna-7b-medusa_0.jsonl
python gen_model_answer_medusa.py  --model-path FasterDecoding/medusa-vicuna-7b-v1.3 --model-id medusa-vicuna-7b-v1.3-0   --answer-file data/mt_bench/experiments/vicuna-7b-medusa_1.jsonl
python gen_model_answer_medusa.py  --model-path FasterDecoding/medusa-vicuna-7b-v1.3 --model-id medusa-vicuna-7b-v1.3-0   --answer-file data/mt_bench/experiments/vicuna-7b-medusa_2.jsonl
python gen_model_answer_medusa.py  --model-path FasterDecoding/medusa-vicuna-7b-v1.3 --model-id medusa-vicuna-7b-v1.3-0   --answer-file data/mt_bench/experiments/vicuna-7b-medusa_3.jsonl
python gen_model_answer_medusa.py  --model-path FasterDecoding/medusa-vicuna-7b-v1.3 --model-id medusa-vicuna-7b-v1.3-0   --answer-file data/mt_bench/experiments/vicuna-7b-medusa_4.jsonl

# baseline 13b
python gen_model_answer_baseline.py  --model-path FasterDecoding/medusa-vicuna-13b-v1.3 --model-id medusa-vicuna-7b-v1.3-0  --answer-file data/mt_bench/experiments/vicuna-13b-baseline0.jsonl
python gen_model_answer_baseline.py  --model-path FasterDecoding/medusa-vicuna-13b-v1.3 --model-id medusa-vicuna-7b-v1.3-0 --answer-file data/mt_bench/experiments/vicuna-13b-baseline1.jsonl
python gen_model_answer_baseline.py  --model-path FasterDecoding/medusa-vicuna-13b-v1.3 --model-id medusa-vicuna-7b-v1.3-0 --answer-file data/mt_bench/experiments/vicuna-13b-baseline2.jsonl

# medusa 13b
python gen_model_answer_medusa.py  --model-path FasterDecoding/medusa-vicuna-13b-v1.3 --model-id medusa-vicuna-13b-v1.3-0  --answer-file data/mt_bench/experiments/vicuna-13b-medusa_0.jsonl --medusa-choices vicuna_13b_stage1
python gen_model_answer_medusa.py  --model-path FasterDecoding/medusa-vicuna-13b-v1.3 --model-id medusa-vicuna-13b-v1.3-0   --answer-file data/mt_bench/experiments/vicuna-13b-medusa_1.jsonl --medusa-choices vicuna_13b_stage1
python gen_model_answer_medusa.py  --model-path FasterDecoding/medusa-vicuna-13b-v1.3 --model-id medusa-vicuna-13b-v1.3-0   --answer-file data/mt_bench/experiments/vicuna-13b-medusa_2.jsonl --medusa-choices vicuna_13b_stage1
python gen_model_answer_medusa.py  --model-path FasterDecoding/medusa-vicuna-13b-v1.3 --model-id medusa-vicuna-13b-v1.3-0   --answer-file data/mt_bench/experiments/vicuna-13b-medusa_3.jsonl --medusa-choices vicuna_13b_stage1
python gen_model_answer_medusa.py  --model-path FasterDecoding/medusa-vicuna-13b-v1.3 --model-id medusa-vicuna-13b-v1.3-0   --answer-file data/mt_bench/experiments/vicuna-13b-medusa_4.jsonl --medusa-choices vicuna_13b_stage1
