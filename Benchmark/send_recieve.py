import os
import time
import signal
import random
from termcolor import cprint
from cohere_api import run_cohere_model
from open_ai_api import run_open_ai_model
from helper_functions import (
    find_last_folder_number,
    set_timeout,
    get_params,
    parameterize_question,
    write_info_file,
    write_response,
    write_prompt_and_model_args,
    create_result_folder,
    rename_model,
    create_model_folder,
    write_param_file,
)


def send_prompt_recieve_response(path, q, r, model_params, seed):
    model_name = model_params["model"]
    if not model_name:
        print("Please specify the model in the config file.")
        exit()
    number_of_parameters = r.get("number_of_parameters")
    shuffle = True if r.get("shuffle").lower() == "true" else False

    OpenAI = ["gpt-3.5-turbo", "gpt-4"]
    cohere = ["command", "command-light"]

    model = rename_model(model_name)

    _, columns = os.popen("stty size", "r").read().split()

    last_number = find_last_folder_number(path + f"/Q{q}", model, True)
    create_model_folder(path + f"/Q{q}", model, last_number)
    params_list = get_params(q, seed)
    if shuffle:
        if seed != "default":
            random.seed(seed)
        random.shuffle(params_list)
    write_param_file(q, model, last_number, params_list)

    c = 1

    params_list = params_list[:number_of_parameters]

    for params in params_list:
        create_result_folder(path + f"/Q{q}", c, model, last_number)
        if type(params) != tuple:
            params = (params,)

        question, function_name = parameterize_question(q, params)
        write_info_file(q, model, c, params, function_name, last_number)

        remainder = c % 10
        if remainder == 1:
            suffix = "st"
        elif remainder == 2:
            suffix = "nd"
        elif remainder == 3:
            suffix = "rd"
        else:
            suffix = "th"

        if q < 10:
            takes_space = 10
        elif 10 <= q < 100:
            takes_space = 11
        else:
            takes_space = 12

        print()
        cprint(
            f"Question {q}" + (" " * ((int(columns) // 2) - takes_space)),
            "black",
            "on_white",
            attrs=["bold"],
        )
        cprint(
            f"{c}{suffix} parameters" + (" " * ((int(columns) // 3) - takes_space)),
            "black",
            "on_light_grey",
            attrs=["bold"],
        )
        print(f"Waiting for {model_name} to respond...")
        sleep_duration = 1
        start_time = 0.0
        response, prompt = "", ""
        while True:
            try:
                start_time = time.time()
                while time.time() - start_time < 5:
                    if model_name in OpenAI:
                        response, prompt = run_open_ai_model(model_params, question)
                    elif model_name in cohere:
                        start_time = time.time()
                        response, prompt = run_cohere_model(model_params, question)
                    break
            except Exception as e:
                print(e)
                cprint(
                    f"{model_name} model did not respond. Retrying in {sleep_duration}(s)...",
                    "light_red",
                )
                time.sleep(sleep_duration)
                sleep_duration *= 2

            else:
                break

        duration = time.time() - start_time
        cprint(f"The {model_name} response was received.", "light_green")
        cprint(f"Time taken: {round(duration, 3)}(s)\n", "light_blue")

        if model_name in OpenAI:
            extention = "json"
        elif model_name in cohere:
            extention = "txt"

        write_response(q, c, model, response, last_number, extention)
        model_params["question"] = question
        model_params["complete_prompt"] = prompt
        write_prompt_and_model_args(q, c, model, model_params, last_number)
        c += 1
