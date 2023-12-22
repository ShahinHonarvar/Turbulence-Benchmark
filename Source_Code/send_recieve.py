import os
import time
import signal
import random
from termcolor import cprint
from ollama import run_ollama_model
from cohere_api import run_cohere_model
from open_ai_api import run_open_ai_model
from helper_functions import (
    get_params,
    set_timeout,
    rename_model,
    write_response,
    write_info_file,
    write_param_file,
    create_model_folder,
    create_result_folder,
    parameterize_question,
    write_prompt_and_model_args,
)


def send_prompt_recieve_response(path, q, r, model_params, seed, num):
    model_name = model_params["model"]
    if not model_name:
        print("Please specify the model in the config file.")
        exit()
    number_of_parameters = r.get("number_of_parameters")
    shuffle = True if r.get("shuffle").lower() == "true" else False

    OpenAI = ["gpt-3.5-turbo", "gpt-4"]
    cohere = ["command"]
    ollama = ["codellama:7b"]

    model = rename_model(model_name)

    _, columns = os.popen("stty size", "r").read().split()

    create_model_folder(path + f"/Q{q}", model, num)
    params_list = get_params(q, seed)
    if shuffle:
        if seed != "default":
            random.seed(seed)
        random.shuffle(params_list)
    write_param_file(q, model, num, params_list)

    c = 1
    params_list = params_list[:number_of_parameters]
    inference_latency = []
    for params in params_list:
        create_result_folder(path + f"/Q{q}", c, model, num)
        if type(params) != tuple:
            params = (params,)

        question, function_name = parameterize_question(q, params)
        write_info_file(q, model, c, params, function_name, num)

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
        timeout = 150
        response, prompt = "", ""
        while True:
            try:
                set_timeout(timeout)
                if model_name in OpenAI:
                    start_time_real = time.time()
                    response, prompt = run_open_ai_model(model_params, question)
                    inference_latency.append(time.time() - start_time_real)

                elif model_name in cohere:
                    start_time_real = time.time()
                    response, prompt = run_cohere_model(model_params, question)
                    inference_latency.append(time.time() - start_time_real)

                if model_name in ollama:
                start_time_real = time.time()
                response, prompt = run_ollama_model(model_params, question)
                inference_latency.append(time.time() - start_time_real)

                break

            except Exception as e:
                cprint(e, "light_red")
                cprint(
                    f"{model_name} model did not respond. Retrying in {sleep_duration}(s)...",
                    "light_red",
                )
                time.sleep(sleep_duration)
                sleep_duration *= 2

            finally:
                signal.alarm(0)

        cprint(f"The {model_name} response was received.", "light_green")
        cprint(
            f"Inference latency: {round(inference_latency[c-1], 3)}(s)\n", "light_blue"
        )

        if model_name in OpenAI:
            extention = "json"
        elif model_name in cohere or model_name in ollama:
            extention = "txt"

        write_response(q, c, model, response, num, extention)
        model_params["question"] = question
        model_params["complete_prompt"] = prompt
        write_prompt_and_model_args(q, c, model, model_params, num)
        c += 1
