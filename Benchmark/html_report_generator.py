import os
import sys
import time
import platform
from pathlib import Path
from helper_functions import rename_model


def write_html_report(path, model_params, seed, questions_req, q_test_result, execution_time, get_generation_time, test_time):
    version = sys.version_info
    os_type = platform.platform()
    model = model_params.get("model")
    max_tokens = model_params.get("max_tokens")
    temperature = model_params.get("temperature")
    presence_penalty = model_params.get("presence_penalty")
    frequency_penalty = model_params.get("frequency_penalty")
    questions = list(questions_req.keys())
    results = ""

    if not get_generation_time:
        get_generation_time = [0 for _ in range(len(questions))]

    if not test_time:
        test_time = [0 for _ in range(len(questions))]

    if model == "fake":
        model_path = "fake"
    else:
        model_path = rename_model(model)
    
    counter = 0
    for q in questions:
        wrong_params = q_test_result[q][0]
        correct_params = q_test_result[q][1]
        last_number = q_test_result[q][2]
        first_portion = q_test_result[q][3]
        second_portion = q_test_result[q][4]
        thersholds = questions_req[q].get(
            "similarity_thresholds").replace(" ", "").split(",")
        higher_threshold = float(thersholds[0])
        lower_threshold = float(thersholds[1])

        link_wrong_params = (
            f'<a href="{path}/Q{q}/{model_path}_results_{last_number}/wrong_params.html" target="_blank">Click to see them.</a>'
            if wrong_params
            else ""
        )

        link_correct_params = (
            f'<a href="{path}/Q{q}/{model_path}_results_{last_number}/correct_params.html" target="_blank">Click to see them.</a>'
            if correct_params
            else ""
        )

        link_first_portion = (
            f'<a href="{path}/Q{q}/{model_path}_results_{last_number}/higher_similarity.html" target="_blank">Click to see them.</a>'
            if first_portion
            else "None"
        )

        link_second_portion = (
            f'<a href="{path}/Q{q}/{model_path}_results_{last_number}/lower_similarity.html" target="_blank">Click to see them.</a>'
            if second_portion
            else "None"
        )

        space = "&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"
        first_portion_second_cell = f"{space}{link_first_portion}" if first_portion else link_first_portion
        second_portion_second_cell = f"{space}{link_second_portion}" if second_portion else link_second_portion
        least = '' if higher_threshold == 1.0 else 'at least'
        result = f"""
        <table style="width:50%" class="question">
        <tr>
            <td>Question {q}</td>
            <td></td>
        </tr>
        <tr>
            <td>Number of parameters</td>
            <td>{questions_req[q].get('number_of_parameters')}</td>
        </tr>
        <tr>
            <td>Parameters shuffle</td>
            <td>{questions_req[q].get('shuffle')}</td>
        </tr>
        <tr>
            <td>Fuzzy testing</td>
            <td>{questions_req[q].get('fuzzy_testing')}</td>
        </tr>
        <tr>
            <td>Number of fuzzy inputs</td>
            <td>{questions_req[q].get('number_of_random_inputs')}</td>
        </tr>
        <tr>
            <td>Fuzzy testing terminates with the first error</td>
            <td>{questions_req[q].get('terminates_with_first_error')}</td>
        </tr>
        <tr>
            <td>Similarity thresholds</td>
            <td>{higher_threshold}, {lower_threshold}</td>
        </tr>
        <tr>
            <td>Results</td>
            <td></td>
        </tr>
        <tr>
            <td>Total time of obtaining generated results from {model}</td>
            <td>{round(get_generation_time[counter], 3)} (s)</td>
        </tr>
        <tr>
            <td>Total test time</td>
            <td>{round(test_time[counter], 3)} (s)</td>
        </tr>
        <tr>
            <td>Number of parameters with which {model_path} generated correct code</td>
            <td>{len(correct_params)}&nbsp&nbsp&nbsp&nbsp&nbsp{link_correct_params}</td>
        </tr>
        <tr>
            <td>Correct code results with similarity of {least} {higher_threshold}</td>
            <td>{first_portion_second_cell}</td>
        </tr>
        <tr>
            <td>Correct code results with similarity between {lower_threshold} and {higher_threshold}</td>
            <td>{second_portion_second_cell}</td>
        </tr>
        <tr>
            <td>Number of parameters with which {model_path} generated wrong code</td>
            <td>{len(wrong_params)}&nbsp&nbsp&nbsp&nbsp&nbsp{link_wrong_params}</td>
        </tr>
        <br></br>
        <br></br>
        """
        results += result
        counter += 1

    content = (
        f"""
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" href="{path}/report_styles.css">
    </head>
    <body>
        <h1>Turbulence Benchmark</h1>
        <table style="width:100%" class="info_table">
            <tr>
                <td>Operating system</td>
                <td>{os_type}</td>
            </tr> 
            <tr>
                <td>Python version</td>
                <td>{version[0]}.{version[1]}.{version[2]}</td>
            </tr>  
            <tr>
                <td>Large language model</td>
                <td>{model} (max_tokens: {max_tokens}, temperature: {temperature}, presence_penalty: {presence_penalty}, frequency_penalty: {frequency_penalty})</td>
            </tr>
            <tr>
            <td>Questions</td>
            <td>{questions}</td>
            </tr>
            <tr>
            <td>Seed value</td>
            <td>{seed}</td>
            </tr>
            <tr>
            <td>Total execution time</td>
            <td>{round(execution_time, 3)} (s)</td>
            </tr>
        </table>
        <br></br>"""
        + results
        + """
    </body>
    </html>
    """
    )

    full_path = path + "/Final_Verdict"
    if not os.path.exists(full_path):
        Path(full_path).mkdir(parents=True, exist_ok=False)
    with open(
        full_path + f'/{model_path}_{time.strftime("%Y%m%d-%H%M%S")}.html', "w"
    ) as f:
        f.write(content)
