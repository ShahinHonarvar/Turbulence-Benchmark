import os
import json
import time
from termcolor import cprint
from benchmark_test import run_test
from html_report_generator import write_html_report
from send_recieve import send_prompt_recieve_response
from helper_functions import extract_questions_params_inputs


start = time.time()
with open("config.json", "r") as f:
    config = json.load(f)

model_specs = config["model_specifications"]
seed = config["seed"]
path = config["path"]
questions_req = extract_questions_params_inputs(config["questions"])

q_total_code_generation_time = []
q_total_test_time = []

for q, r in questions_req.items():
    # q_start = time.time()
    real_latency, total_latency = send_prompt_recieve_response(
        path, q, r, model_specs, seed)
    q_total_code_generation_time.append((real_latency, total_latency))
    # q_end = time.time()
    # q_total_code_generation_time.append(q_end - q_start)


if os.path.exists("model_latency.txt"):
    with open("model_latency.txt", "a") as f:
        for (i, j) in q_total_code_generation_time:
            f.write(f'real time:{i}\n total time:{j}\n')
            f.write('\n\n')
        f.write('='*20)
else:
    with open("model_latency.txt", "w+") as f:
        for (i, j) in q_total_code_generation_time:
            f.write(f'Real time:{i}\nTotal time:{j}\n')
            f.write('\n\n')
        f.write('='*20)
        f.write('\n\n')

# q_test_result = {}
# for q, r in questions_req.items():
#     q_test_start = time.time()
#     q_test_result[q] = run_test(path, q, r, model_specs, seed)
#     q_test_end = time.time()
#     q_total_test_time.append(q_test_end - q_test_start)

# execution_time = time.time() - start
# write_html_report(path, model_specs, seed, questions_req,
#                   q_test_result, execution_time, q_total_code_generation_time, q_total_test_time)

# print()
# cprint(
#     f'Total execution time:    {round(execution_time, 3)} (s).', 'light_blue', attrs=['bold'])
# print()
