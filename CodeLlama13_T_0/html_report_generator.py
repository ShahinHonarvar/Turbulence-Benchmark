import sys
import time
import platform
from helper_functions import rename_model



def write_html_report(path, model_params, seed, q, questions_req, rounds, binary_correctness, number_of_parameters, test_durations):
    version = sys.version_info
    os_type = platform.platform()
    model = model_params.get("model")
    max_tokens = model_params.get("max_tokens")
    temperature = model_params.get("temperature")
    presence_penalty = model_params.get("presence_penalty")
    frequency_penalty = model_params.get("frequency_penalty")
    questions = list(questions_req.keys())
    model_path = rename_model(model)
    
    report_content = f"""
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
        <td>{questions_req[q].get('number_of_fuzzy_inputs')}</td>
    </tr>
    """
    for i in range(len(rounds)):
        corr_round = sum(binary_correctness[i*number_of_parameters:(i+1)*number_of_parameters])
        link_wrong_params = (
        f'<a href="{path}/Q{q}/{model_path}_results_{rounds[i]}/wrong_params.html" target="_blank">Click to see them.</a>'
        if number_of_parameters - corr_round
        else ""
        )
        link_correct_params = (
        f'<a href="{path}/Q{q}/{model_path}_results_{rounds[i]}/correct_params.html" target="_blank">Click to see them.</a>'
        if corr_round
        else ""
        )

        report_content += f"""
        <tr>
            <td>Results of Round {rounds[i]}</td>
            <td></td>
        </tr>
        <tr>
            <td>Number of correct responses</td>
            <td>{corr_round}&nbsp&nbsp&nbsp&nbsp&nbsp{link_correct_params}</td>
        </tr>
        <tr>
            <td>Number of wrong responses</td>
            <td>{number_of_parameters - corr_round}&nbsp&nbsp&nbsp&nbsp&nbsp{link_wrong_params}</td>
        </tr>
        <tr style="border-bottom: 3px solid black;">
            <td>Test duration</td>
            <td>{round(test_durations[i], 3)} (s)</td>
        </tr>
        <br></br>
        """

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
        </table>"""
        + report_content
        + """
    </body>
    </html>
    """
    )

    full_path = path + f"/Q{q}"
    with open(
        full_path + f'/Final_report_{time.strftime("%Y%m%d-%H%M%S")}.html', "w"
    ) as f:
        f.write(content)
