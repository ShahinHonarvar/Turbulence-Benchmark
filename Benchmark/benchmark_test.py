import pytest
from test_plugin import TestResults
from measure_similiarity import similarity_partition
from helper_functions import (
    find_last_folder_number,
    read_file,
    parameterize_model_answer,
    trim_answer,
    create_answer_file,
    is_function,
    compare_param_nums,
    parameterize_tests,
    create_pytest_ini_file,
    create_conftest_file,
    get_random_input,
    get_generated_answer_result,
    get_model_answer_result,
    if_two_lists_are_equal,
    extra_testing_report,
    param_report_file_writer,
    rename_model,
    extract_answer,
    if_two_lists_are_equal_order_irrelevant,
    if_two_matrices_are_equal,
    create_visual_tree,
    create_string_tree,
    higher_similarity_file_writer,
    lower_similarity_file_writer,
)


def run_test(path, q, r, model_params, seed):
    OpenAI = ["gpt-3.5-turbo", "gpt-4"]
    cohere = ["command", "command-light"]
    model_name = model_params["model"]
    model = rename_model(model_name)

    correct_answers = []
    last_number = find_last_folder_number(path + f"/Q{q}", model, False)
    if last_number == 0:
        return

    params_raised_error = {}
    params_not_raised_error = {}
    counter_examples = {}
    correct_random_inputs = []

    c = 1
    number_of_parameters = r.get("number_of_parameters")
    similarity_thresholds = r.get("similarity_thresholds")

    while c <= number_of_parameters:
        counter_examples.clear()
        correct_random_inputs.clear()
        info_dict = read_file(q, model, c, "info", last_number, "json")
        params, function_name = info_dict["params"], info_dict["function_name"]
        parameterize_model_answer(q, c, params, model, last_number)
        generated_answer = ""

        if model_name in OpenAI:
            response_dict = read_file(
                q, model, c, "response", last_number, "json")
            generated_answer = response_dict["choices"][0]["message"]["content"]
            generated_answer = trim_answer(generated_answer)
        elif model_name in cohere:
            response_txt = read_file(
                q, model, c, "response", last_number, "txt")
            generated_answer = extract_answer(response_txt)

        if "def" not in generated_answer:
            params_raised_error[c] = params
            c += 1
            continue

        all_f_names = create_answer_file(
            q, c, generated_answer, model, last_number)

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

        if (
            not is_function(generated_answer)
            or not function_names_equality
            or not compare_param_nums(
                q, c, function_name, f_name, model, params, last_number
            )
        ):
            params_raised_error[c] = params
            c += 1
            continue

        parameterize_tests(q, c, f_name, params, model, last_number)
        create_pytest_ini_file(q, c, model, last_number)
        create_conftest_file(q, c, model, last_number)
        tr = TestResults()
        pytest_params = [
            "-v",
            f"Q{q}/{model}_results_{last_number}/Folder_{c}/tests{q}_{c}_{last_number}.py",
            "-c",
            f"Q{q}/{model}_results_{last_number}/Folder_{c}/Q{q}_{c}.ini",
        ]

        pytest.main(pytest_params, plugins=[tr])
        generated_code_was_wrong = False

        if tr.failed != 0:
            generated_code_was_wrong = True

        if tr.failed == 0 and r.get("fuzzy_testing").lower() == "true":
            number_of_random_inputs = r.get("number_of_fuzzy_inputs")
            generated_answer_result, model_answer_result = "", ""

            for _ in range(number_of_random_inputs):
                r_i = get_random_input(q, params, seed)

                if type(r_i) == tuple and q != 48 and q != 54 and q != 59 and q != 60:
                    random_input = [*r_i]
                else:
                    random_input = [r_i]

                if q == 34:
                    random_input = r_i

                generated_answer_result = get_generated_answer_result(
                    q, c, f_name, model, random_input, last_number
                )

                model_answer_result = get_model_answer_result(
                    q, c, function_name, model, random_input, last_number
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
                        equality_of_answers = if_two_matrices_are_equal(
                            generated_answer_result, model_answer_result
                        )
                    elif q == 55 or q == 56:
                        equality_of_answers = if_two_lists_are_equal_order_irrelevant(
                            generated_answer_result, model_answer_result
                        )
                    else:
                        equality_of_answers = if_two_lists_are_equal(
                            generated_answer_result, model_answer_result
                        )
                else:
                    equality_of_answers = generated_answer_result == model_answer_result

                if not equality_of_answers:
                    generated_code_was_wrong = True
                    if q == 47:
                        counter_examples[
                            tuple(
                                tuple(
                                    (random_input[0])
                                    + ["1000000000000000000001"]
                                    + (random_input[1])
                                )
                            )
                        ] = (model_answer_result, generated_answer_result)
                    else:
                        counter_examples[tuple(*random_input)] = (
                            model_answer_result,
                            generated_answer_result,
                        )
                    if r.get("terminates_with_first_error").lower() == "true":
                        break
                else:
                    correct_random_inputs.append(random_input)

            extra_testing_report(
                q,
                c,
                model,
                last_number,
                number_of_random_inputs,
                counter_examples,
                correct_random_inputs,
            )

        if generated_code_was_wrong:
            params_raised_error[c] = params
        else:
            params_not_raised_error[c] = params
            correct_answers.append((c, generated_answer.rstrip()))
            create_visual_tree(q, c, model, last_number, True)
            create_string_tree(q, c, model, last_number, True)

        c += 1

    param_report_file_writer(
        path,
        q,
        params_raised_error,
        params_not_raised_error,
        counter_examples,
        correct_random_inputs,
        model,
        model_name,
        last_number,
    )

    thresholds_list = similarity_thresholds.replace(" ", "").split(",")
    first_threshold, second_threshold = float(thresholds_list[0]), float(
        thresholds_list[1]
    )
    high_similar_results = []
    lower_similar_results = []
    if correct_answers:
        all_buckets = similarity_partition(correct_answers, first_threshold)
        high_similar_results = [i for i in all_buckets if len(i) > 1]
        high_similar_folder_nums = [
            [tup[0] for tup in sublist] for sublist in high_similar_results
        ]
        if second_threshold:
            non_similar_progs = [i for i in all_buckets if len(i) == 1]
            programs = [i[0] for i in non_similar_progs]
            if programs:
                all_buckets = similarity_partition(programs, second_threshold)
                if len(all_buckets):
                    lower_similar_results = [
                        i for i in all_buckets if len(i) > 1]
                    lower_similar_folder_nums = [
                        [tup[0] for tup in sublist] for sublist in lower_similar_results
                    ]

        if high_similar_folder_nums:
            higher_similarity_file_writer(
                path,
                q,
                model,
                last_number,
                high_similar_folder_nums,
                params_not_raised_error,
                first_threshold,
            )
        if lower_similar_results:
            lower_similarity_file_writer(
                path,
                q,
                model,
                last_number,
                lower_similar_folder_nums,
                params_not_raised_error,
                second_threshold,
            )

    return (
        params_raised_error,
        params_not_raised_error,
        last_number,
        high_similar_results,
        lower_similar_results,
    )
