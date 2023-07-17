import os
import re
import ast
import sys
import json
import signal
import importlib.util
from pathlib import Path
from inspect import signature
from graphviz import Source, Digraph
from anytree import Node, RenderTree



def compare_param_nums(q_no, c, fun_name, f_name, api_name, params, no):
    solution_module = import_preparation(
        "solution", f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/solution.py"
    )
    solution_module_function = getattr(solution_module, fun_name)

    generated_answer_module = import_preparation(
        "generated_answer",
        f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/generated_answer.py",
    )
    generated_answer_module_function = getattr(generated_answer_module, f_name)
    solution_sig = signature(solution_module_function)
    generated_answer_sig = signature(generated_answer_module_function)

    if q_no == 34:
        if (
            len(generated_answer_sig.parameters) == int(params[0])
            or len(generated_answer_sig.parameters) == 1
        ):
            return True
        else:
            return False

    return len(solution_sig.parameters) == len(generated_answer_sig.parameters)


def create_answer_file(q_no, c, answer, api_name, no):
    with open(
        f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/generated_answer.py", "w"
    ) as f:
        f.write(answer)
        function_names = get_all_function_names(answer)
        return function_names


def create_conftest_file(q_no, c, api_name, no):
    with open(f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/conftest.py", "w") as f:
        content = (
            "import platform\n\n\ndef "
            f'pytest_html_report_title(report):\n    report.title = "Question {q_no} with parameters set no. '
            f'{c}"\n\n\ndef pytest_configure(config):\n    config._metadata = '
            '{\n        "Benchmarking framework": "Turbulence",\n        "Operating system": platform.platform(),'
            '\n        "Python version": platform.python_version()\n    }\n\n\n'
            "def pytest_html_results_table_header(cells):\n    cells.pop()\n\n\n"
            "def pytest_html_results_table_row(cells):\n    cells.pop()"
        )
        f.write(content)


def create_init_py_file(q_no, c, api_name, no):
    with open(f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/__init__.py", "w") as _:
        pass


def create_model_folder(path, api_name, no):
    full_path = path + f"/{api_name}_results_{no}"
    Path(full_path).mkdir(parents=True, exist_ok=False)


def create_result_folder(path, c, api_name, no):
    full_path = path + f"/{api_name}_results_{no}/Folder_{c}"
    Path(full_path).mkdir(parents=True, exist_ok=False)


def create_pytest_ini_file(q_no, c, api_name, no):
    with open(f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/Q{q_no}_{c}.ini", "w") as f:
        content = f"[pytest]\naddopts = --html=Q{q_no}/{api_name}_results_{no}/Folder_{c}/pre_existing_test_report.html --report-log=Q{q_no}/{api_name}_results_{no}/Folder_{c}/test_report.json"
        f.write(content)


def create_string_tree(q_no, c, api_name, no, inside_folder):
    with open(
        f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/generated_answer.py", "r"
    ) as f:
        code = f.read()
    tree = ast.parse(code)
    root = Node("Root")

    def create_tree(node, parent):
        ast_node = Node(str(node.__class__.__name__), parent=parent)
        for child in ast.iter_child_nodes(node):
            create_tree(child, ast_node)

    create_tree(tree, root)

    if inside_folder:
        location = f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/text_tree.txt"
    else:
        location = f"Q{q_no}/{api_name}_results_{no}/common_visual_tree.txt"

    with open(location, "w") as f:
        for x, _, node in RenderTree(root):
            f.write("%s%s\n" % (x, node.name))


def create_visual_tree(q_no, c, api_name, no, inside_folder):
    with open(
        f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/generated_answer.py", "r"
    ) as f:
        code = f.read()
    tree = ast.parse(code)

    def create_graph(node, graph):
        node_name = str(node.__class__.__name__)

        # colours available at https://graphviz.org/doc/info/colors.html
        graph.node(
            str(node),
            label=node_name,
            shape="box",
            style="filled, rounded",
            fillcolor="aquamarine3",
        )
        for child in ast.iter_child_nodes(node):
            child_name = str(child.__class__.__name__)
            graph.node(str(child), label=child_name)
            graph.edge(str(node), str(child))
            create_graph(child, graph)

    graph = Digraph()
    create_graph(tree, graph)
    src = Source(graph.source)
    if inside_folder:
        location = f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/visual_tree"
    else:
        location = f"Q{q_no}/{api_name}_results_{no}/common_visual_tree"
    src.render(
        location,
        format="svg",
        view=False,
    )


def extract_answer(txt):
    if "python" in txt:
        txt = txt.replace("python", "")
    if "Python" in txt:
        txt = txt.replace("Python", "")
    idxtext = txt.find("text:")
    idxlike = txt.find("likelihood")
    answer = txt[idxtext + 5 : idxlike]
    if "```" in answer:
        idx0 = answer.find("```")
        idx1 = answer.rfind("```")
        return answer[idx0 + 3 : idx1]
    return answer


def extract_questions_params_inputs(questions_params_inputs):
    q_requirements = {}
    for k, v in questions_params_inputs.items():
        if "," in k:
            comma_split = [i.strip() for i in k.split(",")]
            for x in comma_split:
                if "-" in x:
                    dash_index = x.find("-")
                    start = int(x[:dash_index])
                    stop = int(x[dash_index + 1 :])
                    for i in range(start, stop + 1):
                        q_requirements[i] = v
                else:
                    q_requirements[int(x)] = v
        elif "-" in k:
            dash_index = k.find("-")
            start = int(k[:dash_index])
            stop = int(k[dash_index + 1 :])
            for i in range(start, stop + 1):
                q_requirements[i] = v
        else:
            q_requirements[int(k)] = v

    return dict(sorted(q_requirements.items()))


def extra_testing_report(
    q_no, c, api_name, no, num_of_inputs, counter_example, correct_random_inputs
):
    with open(
        f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/fuzzy_test_report.txt", "w"
    ) as f:
        f.write(
            f"Out of {num_of_inputs} random test input(s), the code returned by LLM passed {len(correct_random_inputs)} times and failed {len(counter_example)} times.\n\n"
        )
        c = 1
        if counter_example:
            f.write("The counter examples were as follows:\n\n")
            for example, answers in counter_example.items():
                if q_no != 41:
                    f.write(f"({c}) With the following counter example:\n")
                    f.write(f"{list(example)}\n")
                else:
                    f.write(f"({c}) With the following counter examples:\n")
                    seperator_idx = example.index("1000000000000000000001")
                    f.write(f"Input 1: {list(example[:seperator_idx])}\n")
                    f.write(f"Input 2: {list(example[seperator_idx + 1:])}\n")
                f.write("\nThe correct answer was:\n")
                f.write(f"{answers[0]}")
                f.write("\n\nBut the LLM code returned:\n")
                f.write(f"{answers[1]}")
                f.write("\n\n")
                f.write("=" * 150)
                f.write("\n\n")
                c += 1
        if correct_random_inputs:
            if q_no != 41:
                correct_random_inputs = flatten_list(correct_random_inputs)
                inp = "input"
            else:
                inp = "inputs"
            f.write(
                f"The test {inp} with which the LLM code passed were as follows:\n\n"
            )
            for random_input in correct_random_inputs:
                f.write(f"({c}) Test {inp}:\n")
                if q_no != 41:
                    f.write(f"{random_input}\n\n")
                else:
                    f.write(f"Input 1: {random_input[0]}\n")
                    f.write(f"Input 2: {random_input[1]}\n\n")
                f.write("=" * 150)
                f.write("\n\n")
                c += 1


def find_last_folder_number(full_path, model, flag):
    all_folders = next(os.walk(full_path))[1]
    result_folders = [f for f in all_folders if f.startswith(f"{model}_results")]
    folder_numbers = []

    if result_folders:
        for f in result_folders:
            dash_idx = f.rfind("_")
            folder_numbers.append(int(f[dash_idx + 1 :]))
        if flag:
            last_number = max(folder_numbers) + 1
        else:
            last_number = max(folder_numbers)
    else:
        if flag:
            last_number = 1
        else:
            last_number = 0

    return last_number


def flatten_list(given_list):
    return [element for sublist in given_list for element in sublist]


def get_all_function_names(text):
    matches = re.findall(r"def\s+(\w+)\(", text)
    return matches


def get_generated_answer_result(q_no, c, fun_name, api_name, input, no):
    module = import_preparation(
        "generated_answer",
        f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/generated_answer.py",
    )
    generated_solution = getattr(module, fun_name)
    return generated_solution(*input)


def get_model_answer_result(q_no, c, fun_name, api_name, input, no):
    module = import_preparation(
        "solution", f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/solution.py"
    )
    model_solution = getattr(module, fun_name)
    return model_solution(*input)


def get_params(q_no, seed):
    module = import_preparation("genparams", f"Q{q_no}/genparams.py")
    return module.gen_params(q_no, seed)


def get_random_input(q_no, l, seed):
    module = import_preparation(
        "gen_function_params", f"Q{q_no}/gen_function_params.py"
    )
    return module.input_generator(l, seed)


def if_two_lists_are_equal(l1, l2):
    if len(l1) != len(l2):
        return False
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True


def if_two_lists_are_equal_order_irrelevant(l1, l2):
    if len(l1) != len(l2):
        return False
    else:
        for i in l1:
            if l1.count(i) != l2.count(i):
                return False
    return True


def if_two_matrices_are_equal(m1, m2):
    if len(m1) != len(m2):
        return False
    list_m1, list_m2 = [], []
    for m in m1:
        if type(m) != list:
            list_m1.append(m.tolist())
    for m in m2:
        if type(m) != list:
            list_m2.append(m.tolist())

    return if_two_lists_are_equal_order_irrelevant(list_m1, list_m2)


def equality_of_lists_of_lists_of_lists(l1, l2):
    i = len(l1) * len(l2)
    c = 0
    while l1 and c <= i:
        j = 0
        while l2 and j < len(l2):
            x, y = l1[0], l2[j]
            if if_two_lists_are_equal_order_irrelevant(x, y):
                l1.remove(x)
                l2.remove(y)
            else:
                j += 1
        c += 1
    if l1 or l2:
        return False
    else:
        return True


def higher_similarity_file_writer(
    path, q_no, api_name, no, bucket, params_not_raised_error, first_threshold
):
    least = '' if first_threshold == 1.0 else 'at least'
    content = f"""
    <!DOCTYPE html>
    <html>
    <body>
    <h1>Correct code results with a similarity of {least} {first_threshold}</h1>
    <table style="border: 2px solid black; border-collapse:collapse">
        <tr style="background-color:green; color:white">
            <th width="200" style="border: 1px solid black; text-align: left">Folder Number</th>
            <th width="200" style="border: 1px solid black; text-align: left">Parameters</th>
            <th width="400" style="border: 1px solid black; text-align: left">Generated Code</th>
            <th width="400" style="border: 1px solid black; text-align: left">Visual Tree of the Generated Code</th>
            <th width="400" style="border: 1px solid black; text-align: left">Text Tree of the Generated Code</th>
        </tr>
    """

    for lst in bucket:
        for i in lst:
            cells = f"""
            <tr>
                <td style="border: 1px solid black";>
                <a href="{path}/Q{q_no}/{api_name}_results_{no}/Folder_{i}" target="_blank">{i}</a>
                </td>
                <td style="border: 1px solid black";>
                {params_not_raised_error.get(i)}
                </td>
                <td style="border: 1px solid black";>
                <a href="{path}/Q{q_no}/{api_name}_results_{no}/Folder_{i}/generated_answer.py" target="_blank"> Click to see the generated code. </a>
                </td>
                <td style="border: 1px solid black";>
                <a href="{path}/Q{q_no}/{api_name}_results_{no}/Folder_{i}/visual_tree.svg" target="_blank"> Click to see the visual tree. </a>
                </td>
                <td style="border: 1px solid black";>
                <a href="{path}/Q{q_no}/{api_name}_results_{no}/Folder_{i}/text_tree.txt" target="_blank"> Click to see the text tree. </a>
                </td>
            </tr>\n
            """
            content += cells
        row = f"""
            <tr style="background-color:lightgreen">
                <td>
                &nbsp;
                </td>
                <td>
                &nbsp;
                </td>
                <td>
                &nbsp;
                </td>
                <td>
                &nbsp;
                </td>
                <td>
                &nbsp;
                </td>
            </tr>\n
            """
        content += row

    with open(f"Q{q_no}/{api_name}_results_{no}/higher_similarity.html", "w") as f:
        f.write(content)


def lower_similarity_file_writer(
    path, q_no, api_name, no, bucket, params_not_raised_error, second_threshold
):
    content = f"""
    <!DOCTYPE html>
    <html>
    <body>
    <h1>Correct code results with a similarity of at least {second_threshold}</h1>
    <table style="border: 2px solid black; border-collapse:collapse">
        <tr style="background-color:green; color:white">
            <th width="200" style="border: 1px solid black; text-align: left">Folder Number</th>
            <th width="200" style="border: 1px solid black; text-align: left">Parameters</th>
            <th width="400" style="border: 1px solid black; text-align: left">Generated Code</th>
            <th width="400" style="border: 1px solid black; text-align: left">Visual Tree of the Generated Code</th>
            <th width="400" style="border: 1px solid black; text-align: left">String Tree of the Generated Code</th>
        </tr>
    """

    for lst in bucket:
        for i in lst:
            cells = f"""
            <tr>
                <td style="border: 1px solid black";>
                <a href="{path}/Q{q_no}/{api_name}_results_{no}/Folder_{i}" target="_blank">{i}</a>
                </td>
                <td style="border: 1px solid black";>
                {params_not_raised_error.get(i)}
                </td>
                <td style="border: 1px solid black";>
                <a href="{path}/Q{q_no}/{api_name}_results_{no}/Folder_{i}/generated_answer.py" target="_blank"> Click to see the generated code. </a>
                </td>
                <td style="border: 1px solid black";>
                <a href="{path}/Q{q_no}/{api_name}_results_{no}/Folder_{i}/visual_tree.svg" target="_blank"> Click to see the visual tree. </a>
                </td>
                <td style="border: 1px solid black";>
                <a href="{path}/Q{q_no}/{api_name}_results_{no}/Folder_{i}/text_tree.txt" target="_blank"> Click to see the visual tree. </a>
                </td>
            </tr>\n
            """
            content += cells
        row = f"""
            <tr style="background-color:lightgreen">
                <td>
                &nbsp;
                </td>
                <td>
                &nbsp;
                </td>
                <td>
                &nbsp;
                </td>
                <td>
                &nbsp;
                </td>
                <td>
                &nbsp;
                </td>
            </tr>\n
            """
        content += row

    with open(f"Q{q_no}/{api_name}_results_{no}/lower_similarity.html", "w") as f:
        f.write(content)


def import_preparation(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def instantiate(template, args):
    for i in range(len(args)):
        template = template.replace(f"${i}", str(args[i]))

    return template


def is_function(answer):
    try:
        tree = ast.parse(answer)
    except SyntaxError:
        return False
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            return True
    return False


def parameterize_model_answer(q_no, c, params, api_name, no):
    with open(f"Q{q_no}/solution.py.template", "r") as f0, open(
        f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/solution.py", "w"
    ) as f1:
        solution_template = f0.read()
        solution = instantiate(solution_template, params)
        f1.write(solution)
        return solution


def parameterize_question(q_no, params):
    with open(f"Q{q_no}/question.txt.template", "r") as f:
        question_template = f.readline().strip("\n")
        function_name = re.search(r"(?<=').*?(?=')", question_template).group(0)
        question = instantiate(question_template, params)
        return question, function_name


def parameterize_tests(q_no, c, function_name, params, api_name, no):
    with open(f"Q{q_no}/tests.py.template", "r") as f0, open(
        f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/tests{q_no}_{c}_{no}.py", "w"
    ) as f1:
        test_template = f0.read()
        modified_params = params.copy()
        modified_params.append(c)
        modified_params.append(function_name)
        modified_params.append(api_name)
        modified_params.append(no)
        f1.write(instantiate(test_template, modified_params))


def param_report_file_writer(
    path,
    q_no,
    params_raised_error,
    params_not_raised_error,
    counter_examples,
    correct_random_inputs,
    api_name,
    model_name,
    no,
):
    main_dict = {"model_name": model_name}
    if not params_raised_error:
        main_dict["wrong"] = 0
    else:
        wrong_dict = {}
        for f_n, p in params_raised_error.items():
            wrong_dict[f"Folder_{f_n}"] = p
        main_dict["wrong"] = wrong_dict

    if not params_not_raised_error:
        main_dict["correct"] = 0
    else:
        correct_dict = {}
        for f_n, p in params_not_raised_error.items():
            correct_dict[f"Folder_{f_n}"] = p
        main_dict["correct"] = correct_dict

    with open(f"Q{q_no}/{api_name}_results_{no}/params_report.json", "w") as f:
        json.dump(main_dict, f, ensure_ascii=False, indent=2)

    content_header = f"""
    <!DOCTYPE html>
    <html>
    <body>\n
    """
    if params_not_raised_error:
        concat = """
        <h1>Parameters with correct generated code</h1>
        <table style="border: 2px solid black; border-collapse:collapse">
            <tr>
                <th width="200" style="border: 1px solid black; text-align: left">Folder Number</th>
                <th width="200" style="border: 1px solid black; text-align: left">Parameters</th>
                <th width="400" style="border: 1px solid black; text-align: left">Link of Pre-Existing Tests Reports</th>
                <th width="400" style="border: 1px solid black; text-align: left">Link of Fuzzy Tests Reports</th>
            </tr>
        """
        for folder, params in params_not_raised_error.items():
            fuzzy_report = (
                f'<a href="{path}/Q{q_no}/{api_name}_results_{no}/Folder_{folder}/fuzzy_test_report.txt" target="_blank"> Click to see fuzzy test report.</a>'
                if correct_random_inputs
                else ""
            )
            cells = f"""
            <tr>
                <td style="border: 1px solid black";>
                <a href="{path}/Q{q_no}/{api_name}_results_{no}/Folder_{folder}" target="_blank">{folder}</a>
                </td>
                <td style="border: 1px solid black";>
                {params}
                </td>
                <td style="border: 1px solid black";>
                <a href="{path}/Q{q_no}/{api_name}_results_{no}/Folder_{folder}/pre_existing_test_report.html" target="_blank"> Click to see pre-existing test report. </a>
                </td>
                <td style="border: 1px solid black";>
                {fuzzy_report}
                </td>

            </tr>\n
            """
            concat += cells

        with open(f"Q{q_no}/{api_name}_results_{no}/correct_params.html", "w") as f:
            f.write(content_header + concat)

    if params_raised_error:
        concat = f"""
        <h1>Parameters with wrong generated code</h1>
        <table style="border: 2px solid black; border-collapse:collapse">
            <tr>
                <th width="200" style="border: 1px solid black; text-align: left">Folder Number</th>
                <th width="200" style="border: 1px solid black; text-align: left">Parameters</th>
                <th width="400" style="border: 1px solid black; text-align: left">Link of Pre-Existing Tests Reports</th>
                <th width="400" style="border: 1px solid black; text-align: left">Link of Fuzzy Tests Reports</th>
            </tr>
        """
        for folder, params in params_raised_error.items():
            fuzzy_report = (
                f'<a href="{path}/Q{q_no}/{api_name}_results_{no}/Folder_{folder}/fuzzy_test_report.txt" target="_blank"> Click to see fuzzy test report.</a>'
                if counter_examples
                else ""
            )
            cells = f"""
            <tr>
                <td width="100" style="border: 1px solid black";>
                <a href="{path}/Q{q_no}/{api_name}_results_{no}/Folder_{folder}" target="_blank">{folder}</a>
                </td>
                <td width="200" style="border: 1px solid black";>
                {params}
                </td>
                <td width="300" style="border: 1px solid black";>
                <a href="{path}/Q{q_no}/{api_name}_results_{no}/Folder_{folder}/pre_existing_test_report.html" target="_blank"> Click to see pre-existing test report. </a>
                </td>
                <td width="300" style="border: 1px solid black";>
                {fuzzy_report}
                </td>
            </tr>\n
            """
            concat += cells

        with open(f"Q{q_no}/{api_name}_results_{no}/wrong_params.html", "w") as f:
            f.write(content_header + concat)


def read_file(q_no, api_name, c, file_name, no, extention):
    with open(
        f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/{file_name}.{extention}", "r"
    ) as f:
        if extention == "json":
            return json.load(f)
        return f.read()


def rename_model(api_name):
    api_name = api_name.replace("-", "_")
    return api_name.replace(".", "_")


def trim_answer(s):
    if "python" in s:
        s = s.replace("python", "")
    if "Python" in s:
        s = s.replace("Python", "")
    first_backtiks_idx = s.find("```")
    s = s[first_backtiks_idx + 3 :]
    if "```" in s:
        return s[0: s.rfind("```")]
    return s


def handle_timeout(signum, frame):
    raise TimeoutError("Timeout occurred.")


def set_timeout(seconds):
    signal.signal(signal.SIGALRM, handle_timeout)
    signal.alarm(seconds)


def write_info_file(q_no, api_name, c, params, function_name, no):
    d = {"params": params, "function_name": function_name}
    with open(f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/info.json", "w") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)


def write_param_file(q, model, last_number, params_list):
    length = len(params_list)
    with open(f"Q{q}/{model}_results_{last_number}/all_params.txt", "w") as f:
        for i in range(length):
            if i != length - 1:
                f.write(f"{str(params_list[i])}\n")
            else:
                f.write(str(params_list[i]))


def write_prompt_and_model_args(q_no, c, model, models_params, last_number):
    with open(
        f"Q{q_no}/{model}_results_{last_number}/Folder_{c}/model_specs_prompt.json", "w"
    ) as f:
        json.dump(models_params, f, ensure_ascii=False, indent=2)


def write_response(q_no, c, api_name, answer, no, extension):
    with open(
        f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/response.{extension}", "w"
    ) as f:
        f.write(str(answer))
