import os
import time
import psutil
import pytest
from termcolor import cprint
from radon.raw import analyze
from test_plugin import TestResults
from radon.metrics import h_visit, mi_parameters
from multiprocessing import Process, SimpleQueue
from helper_functions import (
    checker,
    get_rank,
    read_file,
    is_function,
    rename_model,
    extract_code,
    extract_answer,
    get_random_input,
    create_visual_tree,
    create_string_tree,
    create_answer_file,
    compare_param_nums,
    parameterize_tests,
    create_conftest_file,
    extra_testing_report,
    create_pytest_ini_file,
    if_two_lists_are_equal,
    get_model_answer_result,
    param_report_file_writer,
    write_complexity_reports,
    parameterize_model_answer,
    get_generated_answer_result,
    write_test_cases_json_report,
    if_two_lists_of_matrices_are_equal,
    wrong_params_failure_reasons_writer,
    if_two_lists_are_equal_order_irrelevant,
)


def monitor_time_space(pid, available_mem, start_time, allowed_time, q):
    while True:
        try:
            if not psutil.pid_exists(pid):
                q.put("done")
                cprint(
                    "Done.",
                    "blue",
                    "on_black",
                    attrs=["bold"],
                )
                break
            
            if psutil.virtual_memory()[1] < available_mem * (10**9):
                os.kill(pid, 9)
                q.put("High memory usage.")
                cprint(
                    "High memory usage.\n",
                    "red",
                    "on_black",
                    attrs=["bold"],
                )
                break

            if time.time() - start_time > allowed_time:
                os.kill(pid, 9)
                q.put("High execution runtime.")
                cprint(
                    "High execution runtime.\n",
                    "red",
                    "on_black",
                    attrs=["bold"],
                )
                break

            time.sleep(0.000005)

        except Exception as e:
            q.put(e)
            cprint(
                f"{e}\n",
                "red",
                "on_black",
                attrs=["bold"],
            )
            break


def run_test(path, q, r, model_params, num):
    c = 1
    wrong_answers = []
    correct_answers = []
    counter_examples = {}
    parsable_answers = []
    binary_correctness = []
    params_raised_error = {}
    correct_random_inputs = []
    timeout = r.get("timeout")
    params_not_raised_error = {}
    model_name = model_params["model"]
    model = rename_model(model_name)
    ollama = ["codellama:7b"]
    OpenAI = ["gpt-3.5-turbo", "gpt-4"]
    number_of_parameters = r.get("number_of_parameters")
    minimum_available_memory = r.get("minimum_available_memory")

    while c <= number_of_parameters:
        cprint(
            f"\n{5*'>'} Question {q}, instance no. {c}\n",
            "cyan",
            attrs=["bold"],
        )
        generated_answer = ""
        counter_examples.clear()
        correct_random_inputs.clear()
        info_dict = read_file(q, model, c, "info", num, "json")
        params, function_name = info_dict["params"], info_dict["function_name"]
        parameterize_model_answer(q, c, params, model, num)

        if model_name in OpenAI:
            response_dict = read_file(q, model, c, "response", num, "json")
            generated_answer = response_dict["choices"][0]["message"]["content"]
            generated_answer = extract_code(generated_answer, function_name)

        elif model_name == "command":
            response_txt = read_file(q, model, c, "response", num, "txt")
            generated_answer = extract_answer(response_txt)

        elif model_name in ollama:
            response_txt = read_file(q, model, c, "response", num, "txt")
            generated_answer = extract_code(response_txt, function_name)
        

        if "def" not in generated_answer:
            params_raised_error[c] = (
                params,
                False,
                False,
                "No Python function was generated.",
            )
            wrong_answers.append(generated_answer)
            binary_correctness.append(0)
            c += 1
            continue

        all_f_names = create_answer_file(q, c, generated_answer, model, num)

        error_checking_result = checker(q, c, model, num)
        
        if error_checking_result:
            if error_checking_result != "syntax-error":
                parsable_answers.append(generated_answer)
            params_raised_error[c] = (
                params,
                False,
                False,
                f"Linting error: {error_checking_result}",
            )
            wrong_answers.append(generated_answer)
            binary_correctness.append(0)
            c += 1
            cprint(
                (f"FAIL: {error_checking_result}.\n"),
                "red",
                "on_black",
                attrs=["bold"],
            )
            continue

        f_name = ""
        function_names_equality = False
        if len(all_f_names) == 1:
            if all_f_names[0] == function_name:
                function_names_equality = True
                f_name = all_f_names[0]
        else:
            for name in all_f_names:
                if name == function_name:
                    function_names_equality = True
                    f_name = name
                    break

        if not is_function(generated_answer):

            params_raised_error[c] = (
                params,
                False,
                False,
                "The generated response was not a function.",
            )
            wrong_answers.append(generated_answer)
            binary_correctness.append(0)
            c += 1
            cprint(
                ("FAIL: The generated response was not a function.\n"),
                "red",
                "on_black",
                attrs=["bold"],
            )
            continue

        if not function_names_equality:
            params_raised_error[c] = (
                params,
                False,
                False,
                "The generated function did not have the specified name.",
            )
            parsable_answers.append(generated_answer)
            wrong_answers.append(generated_answer)
            binary_correctness.append(0)
            c += 1
            cprint(
                ("FAIL: The generated function did not have the specified name.\n"),
                "red",
                "on_black",
                attrs=["bold"],
            )
            continue

        if not compare_param_nums(q, c, function_name, f_name, model, params, num):
            params_raised_error[c] = (
                params,
                False,
                False,
                "The number of parameters in the function signature was wrong.",
            )
            
            wrong_answers.append(generated_answer)
            binary_correctness.append(0)
            c += 1
            cprint(
                (
                    "FAIL: The number of parameters in the function signature was wrong.\n"
                ),
                "red",
                "on_black",
                attrs=["bold"],
            )
            continue

        parameterize_tests(q, c, f_name, params, model, num)
        create_pytest_ini_file(q, c, model, num, timeout)
        create_conftest_file(q, c, model, num)
        tr = TestResults()
        pytest_params = [
            "-v",
            f"Q{q}/{model}_results_{num}/Folder_{c}/tests{q}_{c}_{num}.py",
            "-c",
            f"Q{q}/{model}_results_{num}/Folder_{c}/Q{q}_{c}.ini",
        ]

        generated_code_is_correct = True

        try:
            pytest.main(pytest_params, plugins=[tr])

        except Exception as e:
            print(e)
            generated_code_is_correct = False
        
        write_test_cases_json_report(q, model, c, params, num)
        if tr.failed != 0:
            generated_code_is_correct = False
            params_raised_error[c] = (
                params,
                True,
                False,
                "Check the pre-existing tests report.",
            )

        if generated_code_is_correct and r.get("fuzzy_testing").lower() == "true":
            cprint(
                ("\nStart fuzzy testing...\n"),
                "blue",
                "on_black",
                attrs=["bold"],
            )

            number_of_random_inputs = r.get("number_of_fuzzy_inputs")
            generated_answer_result, model_answer_result = "", ""

            for i in range(number_of_random_inputs):
                failed_before_testing = False
                cprint(
                    f"\nRandom input no. {i + 1}",
                    "white",
                    "on_black",
                    attrs=["bold"],
                )
                r_i = get_random_input(q, params, i)

                if type(r_i) == tuple and q != 48 and q != 54 and q != 59 and q != 60:
                    random_input = [*r_i]
                else:
                    random_input = [r_i]

                if q == 34:
                    random_input = r_i

                monitor_q = SimpleQueue()
                fuzzy_testing_q = SimpleQueue()
                execution_time_q = SimpleQueue()

                fuzzy_testing_process = Process(
                    target=get_generated_answer_result,
                    args=(
                        q,
                        c,
                        f_name,
                        model,
                        random_input,
                        num,
                        fuzzy_testing_q,
                        execution_time_q,
                    ),
                )

                start_time = time.time()
                fuzzy_testing_process.start()
                pid = fuzzy_testing_process.pid

                monitor_process = Process(
                    target=monitor_time_space,
                    args=(
                        pid,
                        minimum_available_memory,
                        start_time,
                        timeout,
                        monitor_q,
                    ),
                )

                monitor_process.start()
                fuzzy_testing_process.join()
                monitor_process.join()
                monitor_process_result = monitor_q.get()
                equality_of_answers = False

                if monitor_process_result != "done":
                    params_raised_error[c] = (
                        params,
                        False,
                        True,
                        monitor_process_result,
                    )
                    generated_code_is_correct = False
                    failed_before_testing = True

                else:
                    generated_answer_result = fuzzy_testing_q.get()
                    
                    if isinstance(generated_answer_result, str) and generated_answer_result.startswith("exception"):
                        params_raised_error[c] = (
                            params,
                            False,
                            True,
                            f"LLM's code raised {generated_answer_result}",
                        )
                        generated_code_is_correct = False
                    else:
                        generated_answer_duration = execution_time_q.get()
                        equality_of_answers = False
                        model_answer_result = get_model_answer_result(
                            q, c, function_name, model, random_input, num
                        )

                        if type(model_answer_result) == list:
                            if q == 54 or q == 59 or q == 60:
                                equality_of_answers = (
                                generated_answer_result == model_answer_result
                            )
                            elif q == 48:
                                equality_of_answers = (
                                generated_answer_result.upper() == model_answer_result
                            )
                            elif q == 57:
                                equality_of_answers = if_two_lists_of_matrices_are_equal(
                                generated_answer_result, model_answer_result
                            )
                            elif q == 55 or q == 56:
                                equality_of_answers = (
                                if_two_lists_are_equal_order_irrelevant(
                                    generated_answer_result, model_answer_result
                                )
                            )
                            else:
                                equality_of_answers = if_two_lists_are_equal(
                                generated_answer_result, model_answer_result
                            )
                        else:
                            equality_of_answers = (
                            generated_answer_result == model_answer_result
                        )

                        if not equality_of_answers:
                            params_raised_error[c] = (
                            params,
                            False,
                            True,
                            generated_answer_duration,
                            "Check fuzzy test report.",
                        )
                            generated_code_is_correct = False

                if not generated_code_is_correct:
                    if q == 41:
                        counter_examples[
                            tuple(
                                tuple(
                                    (random_input[0])
                                    + ["1000000000000000000001"]
                                    + (random_input[1])
                                )
                            )
                        ] = (model_answer_result, generated_answer_result)

                    elif q in [
                        22,
                        23,
                        24,
                        28,
                        30,
                        32,
                        33,
                        35,
                        36,
                        37,
                        39,
                        40,
                        45,
                        47,
                        49,
                        52,
                        53,
                        56,
                    ]:
                        counter_examples[tuple(random_input)] = (
                            model_answer_result,
                            generated_answer_result,
                        )

                    elif q == 34:
                        c_exa = []
                        for x in random_input:
                            c_exa.append(frozenset(x))
                        counter_examples[tuple(c_exa)] = (
                            model_answer_result,
                            generated_answer_result,
                        )

                    elif q == 57 or q == 58:
                        counter_examples[str(*random_input)] = (
                            model_answer_result,
                            generated_answer_result,
                        )

                    else:
                        counter_examples[tuple(*random_input)] = (
                            model_answer_result,
                            generated_answer_result,
                        )
                    break
                else:
                    correct_random_inputs.append(random_input)

            extra_testing_report(
                q,
                c,
                model,
                num,
                counter_examples,
                correct_random_inputs,
                failed_before_testing,
            )

        if not generated_code_is_correct:
            wrong_answers.append(generated_answer)
            binary_correctness.append(0)

        else:
            correct_answers.append((c, generated_answer.rstrip()))
            create_visual_tree(q, c, model, num, True)
            create_string_tree(q, c, model, num, True)
            binary_correctness.append(1)
            halstead_report = h_visit(generated_answer)._asdict()
            halstead_dict = {
                "h1": halstead_report["total"][0],
                "h2": halstead_report["total"][1],
                "N1": halstead_report["total"][2],
                "N2": halstead_report["total"][3],
                "h": halstead_report["total"][4],
                "N": halstead_report["total"][5],
                "calculated_length": round(halstead_report["total"][6], 3),
                "volume": round(halstead_report["total"][7], 3),
                "difficulty": round(halstead_report["total"][8], 3),
                "effort": round(halstead_report["total"][9], 3),
                "time": round(halstead_report["total"][10], 3),
                "bugs": round(halstead_report["total"][11], 3),
            }
            mi_report = mi_parameters(generated_answer)
            mi_dict = {
                "halstead_volume": mi_report[0],
                "cyclomatic_complexity": mi_report[1],
                "number_of_LLOC": mi_report[2],
                "percent_of_lines_of_comment": mi_report[3],
            }
            raw_analysis = analyze(generated_answer)
            raw_dict = {
                "loc": raw_analysis[0],
                "lloc": raw_analysis[1],
                "sloc": raw_analysis[2],
                "comments": raw_analysis[3],
                "multi": raw_analysis[4],
                "blank": raw_analysis[5],
                "single_comments": raw_analysis[6],
            }
            
            write_complexity_reports(q, c, model, num, halstead_dict, mi_dict, raw_dict)
            params_not_raised_error[c] = (
                params,
                generated_answer_duration,
                halstead_dict,
                mi_dict,
                raw_dict,
                get_rank(mi_report[1]),
            )
        
        c += 1

    if params_raised_error:
        wrong_params_failure_reasons_writer(q, model, params_raised_error, num)

    param_report_file_writer(
        path,
        q,
        params_raised_error,
        params_not_raised_error,
        model,
        model_name,
        num,
    )
    
    return binary_correctness