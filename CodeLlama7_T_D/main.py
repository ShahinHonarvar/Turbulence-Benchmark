import math
import json
import time
from benchmark_test import run_test
from html_report_generator import write_html_report
from send_recieve import send_prompt_recieve_response
from helper_functions import (
    extract_questions_params_inputs,
    extract_result_folder_numbers,
)


start = time.time()
with open("config.json", "r") as f:
    config = json.load(f)

task = config["task"]
model_specs = config["model_specifications"]
seed = config["seed"]
path = config["path"]
questions_req = extract_questions_params_inputs(config["questions"])
number_of_rounds = extract_result_folder_numbers(config["number_of_rounds"])
number_of_correctr_answers = 0
if task == "call_llm":
    for q, r in questions_req.items():
        for num in number_of_rounds:
            send_prompt_recieve_response(path, q, r, model_specs, seed, num)
    
elif task == "test":
    for q, r in questions_req.items():
        test_durations = []
        binary_correctness = []
        number_of_parameters = r.get("number_of_parameters")
        all_runs_q_test_start = time.time()
        
        for num in number_of_rounds:
            test_start = time.time()
            binary_correctness += run_test(path, q, r, model_specs, num)
            test_durations.append(time.time() - test_start)

        write_html_report(
            path,
            model_specs,
            seed,
            q,
            questions_req,
            number_of_rounds,
            binary_correctness,
            number_of_parameters,
            test_durations
        )
        number_of_all_trials = len(number_of_rounds) * number_of_parameters
        corr_sc = sum(binary_correctness) / number_of_all_trials

        standard_deviation = math.sqrt(number_of_all_trials * corr_sc * (1 - corr_sc))
        standard_error = math.sqrt(corr_sc * (1 - corr_sc) / number_of_all_trials)

        all_runs_q_test_end = time.time()
        report_content = {
            "Question": q,
            "CorrSc": corr_sc,
            "Standard_Deviation": standard_deviation,
            "Standard_Error": standard_error,
            "Distribution": binary_correctness,
            "Time": all_runs_q_test_end - all_runs_q_test_start,
        }

        with open(f"Q{q}/Q{q}_stats.json", "w") as f:
            json.dump(report_content, f, ensure_ascii=False, indent=2)
