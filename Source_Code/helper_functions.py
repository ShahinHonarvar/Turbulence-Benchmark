import os
import re
import ast
import sys
import math
import time
import json
import signal
import numpy as np
import importlib.util
from io import StringIO
from pathlib import Path
from pylint.lint import Run
from inspect import signature
from graphviz import Source, Digraph
from anytree import Node, RenderTree
from pylint.reporters import JSONReporter


def calculate_deviation(lst):
    sum_result = 0
    mean = sum(lst) / len(lst)
    for i in lst:
        sum_result += pow(i - mean, 2)

    return math.sqrt(sum_result / len(lst))


def checker(q_no, c, api_name, no):
    reporter = StringIO()
    Run(
        [f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/generated_answer.py"],
        reporter=JSONReporter(reporter),
        exit=False,
    )
    results = json.loads(reporter.getvalue())
    for i in results:
        if i.get("message-id").startswith("E"):
            return i.get("message")
    return None


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


def create_pytest_ini_file(q_no, c, api_name, no, timeout):
    with open(f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/Q{q_no}_{c}.ini", "w") as f:
        content = f"[pytest]\naddopts = -p no:warnings -n 2 --maxfail=1 --timeout={timeout} --report-log=Q{q_no}/{api_name}_results_{no}/Folder_{c}/test_report.json"
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


def delete_redundant(txt):
    lines = txt.split("\n")
    new_lines = []
    for line in lines:
        if (
            line.startswith(" ")
            or line.startswith("@")
            or line.startswith("def")
            or line.startswith("from")
            or line.startswith("import")
        ):
            new_lines.append(line)
            new_lines.append("\n")

    return "".join(new_lines)


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
        answer = answer[idx0 + 3 : idx1]

    return delete_redundant(answer)


def extract_code(txt, function_name):
    if "python" in txt:
        txt = txt.replace("python", "")
    if "Python" in txt:
        txt = txt.replace("Python", "")
    if "```" in txt:
        idx0 = txt.find("```")
        txt = txt[idx0 + 3:]
    
    lines = txt.split('\n')
    indices = [index for (index, item) in enumerate(lines) if f"def {function_name}" in item]
    if len(indices) > 1:
        lines = lines[:indices[1]]
    pure_code = []
    flag = False
    for i in range(len(lines) - 1, -1, -1):
        if not flag:
            if lines[i].startswith(' ') and 'return' in lines[i]:
                flag = True
                pure_code.append(lines[i])
        else:
            pure_code.append(lines[i])

    pure_code = pure_code[::-1]
    result = ''.join([i + '\n' for i in pure_code])

    return result


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


def extract_result_folder_numbers(result_folder):
    nums = []
    if "," in result_folder:
        comma_split = [i.strip() for i in result_folder.split(",")]
        for x in comma_split:
            if "-" in x:
                dash_index = x.find("-")
                start = int(x[:dash_index])
                stop = int(x[dash_index + 1 :])
                for i in range(start, stop + 1):
                    nums.append(int(i))
            else:
                nums.append(int(x))
    elif "-" in result_folder:
        dash_index = result_folder.find("-")
        start = int(result_folder[:dash_index])
        stop = int(result_folder[dash_index + 1 :])
        for i in range(start, stop + 1):
            nums.append(int(i))
    else:
        nums.append(int(result_folder.strip()))

    return sorted(nums)


def extra_testing_report(
    q_no,
    c,
    api_name,
    no,
    counter_example,
    correct_random_inputs,
    failed_before_testing=False,
):
    with open(
        f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/fuzzy_test_report.txt", "w"
    ) as f:
        f.write(
            f"Out of {len(correct_random_inputs) + len(counter_example)} random test input(s), the code returned by LLM passed {len(correct_random_inputs)} times and failed {len(counter_example)} times.\n\n"
        )
        c = 1
        if counter_example:
            f.write("The counter examples were as follows:\n\n")
            for example, answers in counter_example.items():
                if q_no == 57:
                    f.write(f"({c}) With the following counter example:\n")
                    f.write(f"{example}\n")
                elif q_no == 41:
                    f.write(f"({c}) With the following counter examples:\n")
                    seperator_idx = example.index("1000000000000000000001")
                    f.write(f"Input 1: {list(example[:seperator_idx])}\n")
                    f.write(f"Input 2: {list(example[seperator_idx + 1:])}\n")
                else:
                    f.write(f"({c}) With the following counter example:\n")
                    f.write(f"{list(example)}\n")

                if not failed_before_testing:
                    f.write("\nThe correct answer was:\n")
                    if q_no == 57:
                        f.write(f"{answers[0]}")
                        f.write("\n\nBut the LLM code returned:\n")
                        f.write(f"{answers[1]}")
                    else:
                        f.write(f"{answers[0]}")
                        f.write("\n\nBut the LLM code returned:\n")
                        f.write(f"{answers[1]}")
                    f.write("\n\n")
                    f.write("=" * 150)
                    f.write("\n\n")
                    c += 1

        if correct_random_inputs:
            if q_no == 41:
                inp = "inputs"

            else:
                correct_random_inputs = flatten_list(correct_random_inputs)
                inp = "input"

            f.write(
                f"The test {inp} with which the LLM code passed were as follows:\n\n"
            )
            for random_input in correct_random_inputs:
                f.write(f"({c}) Test {inp}:\n")
                if q_no == 41:
                    f.write(f"Input 1: {random_input[0]}\n")
                    f.write(f"Input 2: {random_input[1]}\n\n")
                elif q_no == 57:
                    f.write(f"{random_input}\n\n")
                else:
                    f.write(f"{random_input}\n\n")
                f.write("=" * 150)
                f.write("\n\n")
                c += 1


def flatten_list(given_list):
    return [element for sublist in given_list for element in sublist]


def get_all_function_names(text):
    matches = re.findall(r"def\s+(\w+)\(", text)
    return matches


def get_generated_answer_result(
    q_no, c, fun_name, api_name, input, no, fuzzy_testing_q, execution_time_q
):  
    try:
        module = import_preparation(
        "generated_answer",
        f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/generated_answer.py",
    )
        generated_solution = getattr(module, fun_name)
        start = time.time()
        result = generated_solution(*input)
        duration = time.time() - start
        
    except Exception as e:
        print(f"Exception in the LLM's generated code: {e}")
        fuzzy_testing_q.put(f'exception:{e}')

    else:
        fuzzy_testing_q.put(result)
        execution_time_q.put(duration)
    

def get_model_answer_result(q_no, c, fun_name, api_name, input, no):
    module = import_preparation(
        "solution", f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/solution.py"
    )
    model_solution = getattr(module, fun_name)
    result = model_solution(*input)
    return result


def get_params(q_no, seed):
    module = import_preparation("genparams", f"Q{q_no}/genparams.py")
    return module.gen_params(q_no, seed)


def get_random_input(q_no, l, i):
    module = import_preparation(
        "gen_function_params", f"Q{q_no}/gen_function_params.py"
    )
    return module.input_generator(l, i)


def get_rank(num):
    if 1 <= num <= 5:
        return 'A'
    elif 6 <= num <= 10:
        return 'B'
    elif 11 <= num <= 20:
        return 'C'
    elif 21 <= num <= 30:
        return 'D'
    elif 31 <= num <= 40:
        return 'E'
    else:
        return 'F'
    

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


def if_two_lists_of_matrices_are_equal(l1, original_l2):
    l2 = [np.array(m) for m in original_l2]
    if len(l1) != len(original_l2):
        return False
    for m1 in l1:
        c = len(l2)
        pointer = 0
        while l2 and c > 0:
            m2 = l2[pointer]
            if np.array_equal(m1, m2):
                del l2[pointer]
            else:
                pointer += 1
            c -= 1

    return False if l2 else True


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


def find_file_name(directory, part_of_name):
    files_in_directory = os.listdir(directory)
    desired_files = [file for file in files_in_directory if file.endswith(part_of_name)]

    return desired_files[0]


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
    api_name,
    model_name,
    no,
):
    main_dict = {"model_name": model_name}
    if not params_raised_error:
        main_dict["wrong"] = 0
    else:
        wrong_dict = {}
        for f_n, v in params_raised_error.items():
            wrong_dict[f"Folder_{f_n}"] = v[0]
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
            <tr style="background-color:green; color:white">
                <th width="75" style="border: 1px solid black; text-align: center">Folder Number</th>
                <th width="150" style="border: 1px solid black; text-align: center">Parameters</th>
                <th width="350" style="border: 1px solid black; text-align: center">Link of Pre-Existing Tests Reports</th>
                <th width="350" style="border: 1px solid black; text-align: center">Link of Fuzzy Tests Reports</th>
                <th width="280" style="border: 1px solid black; text-align: center">Code Analysis</th>
                <th width="350" style="border: 1px solid black; text-align: center">Halstead Complexity Measures</th>
                <th width="210" style="border: 1px solid black; text-align: center">Cyclomatic Complexity</th>
            </tr>
        """
        for folder, tup in params_not_raised_error.items():
            cells = f"""
            <tr>
                <td style="border: 1px solid black; text-align: center">
                <a href="{path}/Q{q_no}/{api_name}_results_{no}/Folder_{folder}" target="_blank">{folder}</a>
                </td>
                <td style="border: 1px solid black; text-align: center">
                {tup[0]}
                </td>
                <td style="border: 1px solid black";>
                <a href="{path}/Q{q_no}/{api_name}_results_{no}/Folder_{folder}/pre_existing_test_report.html" target="_blank"> Click to see pre-existing test report. </a>
                </td>
                <td style="border: 1px solid black";>
                <a href="{path}/Q{q_no}/{api_name}_results_{no}/Folder_{folder}/fuzzy_test_report.txt" target="_blank"> Click to see fuzzy test report.</a>
                </td>
                <td style="border: 1px solid black";>
                LOC: {tup[4]['loc']}<br>
                LLOC: {tup[4]['lloc']}<br>
                SLOC: {tup[4]['sloc']}<br>
                Comments: {tup[4]['comments']}<br>
                Multi: {tup[4]['multi']}<br>
                Blank: {tup[4]['blank']}<br>
                Single comments: {tup[4]['single_comments']}<br>
                </td>
                <td style="border: 1px solid black";>
                <br>
                h1: {tup[2]['h1']}<br>
                h2: {tup[2]['h2']}<br>
                N1: {tup[2]['N1']}<br>
                N2: {tup[2]['N1']}<br>
                h: {tup[2]['h']}<br>
                N: {tup[2]['N']}<br>
                Calculated length: {tup[2]['calculated_length']}<br>
                Volume: {tup[2]['volume']}<br>
                Difficulty: {tup[2]['difficulty']}<br>
                Effort: {tup[2]['effort']}<br>
                Time: {tup[2]['time']}<br>
                Bugs: {tup[2]['bugs']}<br>
                <br>
                </td>
                <td style="border: 1px solid black";>
                Score: {tup[3]['cyclomatic_complexity']}<br>
                Rank: {tup[5]}
                </td>
            </tr>\n
            """
            concat += cells
        concat += "</table>"

        explanation = """
        <br>
        <p><b>Code Analysis</b></p>
        <p>LOC: The number of lines of code (total)</p>
        <p>LLOC: The number of logical lines of code</p>
        <p>SLOC: The number of source lines of code (not necessarily corresponding to the LLOC)</p>
        <p>Comments: The number of Python comment lines</p>
        <p>Multi: The number of lines which represent multi-line strings</p>
        <p>Single_comments: The number of lines which are just comments with no code</p>
        <p>Blank: The number of blank lines (or whitespace-only ones)</p>
        <p>---------------------------------------------------------------------------------------------------------------------------</p>
        <p><b>Halstead Complexity Measures</b></p>
        <p>h1: the number of distinct operators</p>
        <p>h2: the number of distinct operands</p>
        <p>N1: the total number of operators</p>
        <p>N2: the total number of operands</p>
        <p>h: the vocabulary, i.e. h1 + h2</p>
        <p>N: the length, i.e. N1 + N2</p>
        <p>calculated_length: h1 * log2(h1) + h2 * log2(h2)</p>
        <p>volume: V = N * log2(h)</p>
        <p>difficulty: D = h1 / 2 * N2 / h2</p>
        <p>effort: E = D * V</p>
        <p>time: T = E / 18 seconds</p>
        <p>bugs: B = V / 3000 - an estimate of the errors in the implementation</p>
        <p>---------------------------------------------------------------------------------------------------------------------------</p>
        <p><b>Cyclomatic Complexity Measures</b></p>
        <p>1 - 5&nbsp;&nbsp;&nbsp;A (low risk - simple block)</p>
        <p>6 - 10&nbsp;&nbsp;&nbsp;B (low risk - well structured and stable block)</p>
        <p>11 - 20&nbsp;&nbsp;&nbsp;C (moderate risk - slightly complex block)</p>
        <p>21 - 30&nbsp;&nbsp;&nbsp;D (more than moderate risk - more complex block)</p>
        <p>31 - 40&nbsp;&nbsp;&nbsp;E (high risk - complex block, alarming)</p>
        <p>41+  F&nbsp;&nbsp;&nbsp;(very high risk - error-prone, unstable block)</p>
        <p></p>
        <a href=https://radon.readthedocs.io/en/latest/api.html#module-radon.complexity>Reference</a>
        """

        with open(f"Q{q_no}/{api_name}_results_{no}/correct_params.html", "w") as f:
            f.write(content_header + concat + explanation)

    if params_raised_error:
        concat = f"""
        <h1>Parameters with wrong generated code</h1>
        <table style="border: 2px solid black; border-collapse:collapse">
            <tr style="background-color:FireBrick; color:white">
                <th width="200" style="border: 1px solid black; text-align: left">Folder Number</th>
                <th width="200" style="border: 1px solid black; text-align: left">Parameters</th>
                <th width="400" style="border: 1px solid black; text-align: left">Link of Pre-Existing Tests Reports</th>
                <th width="420" style="border: 1px solid black; text-align: left">Link of Fuzzy Tests Reports</th>
                <th width="400" style="border: 1px solid black; text-align: left">Test Failure Reason</th>
            </tr>
        """
        for folder, tup in params_raised_error.items():
            
            test_cases_report = (
                f'<a href="{path}/Q{q_no}/{api_name}_results_{no}/Folder_{folder}/pre_existing_test_case_report.json" target="_blank"> Click to see pre-existing test report. </a>'
                if tup[1]
                else ""
            )
            fuzzy_report = (
                f'<a href="{path}/Q{q_no}/{api_name}_results_{no}/Folder_{folder}/fuzzy_test_report.txt" target="_blank"> Click to see fuzzy test report.</a>'
                if tup[2]
                else ""
            )
            cells = f"""
            <tr>
                <td style="border: 1px solid black";>
                <a href="{path}/Q{q_no}/{api_name}_results_{no}/Folder_{folder}" target="_blank">{folder}</a>
                </td>
                <td style="border: 1px solid black";>
                {tup[0]}
                </td>
                <td style="border: 1px solid black";>
                {test_cases_report}
                </td>
                <td style="border: 1px solid black";>
                {fuzzy_report}
                </td>
                <td style="border: 1px solid black";>
                {tup[-1]}
                </td>
            </tr>\n
            """
            concat += cells

        concat += "</table>"

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
    chars = ["-", ".", ":"]
    for char in chars:
        api_name = api_name.replace(char, "_")
    return api_name


def trim_answer(s):
    if "python" in s:
        s = s.replace("python", "")
    if "Python" in s:
        s = s.replace("Python", "")
    first_backtiks_idx = s.find("```")
    s = s[first_backtiks_idx + 3 :]
    if "```" in s:
        s = s[0 : s.rfind("```")]

    return delete_redundant(s)


def handle_timeout(signum, frame):
    raise Exception("Timeout occurred.")


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


def write_complexity_reports(q_no, c, api_name, no, halstead_dict, mi_dict, raw_dict):
    with open(
        f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/halstead_report.json", "w"
    ) as f0, open(
        f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/mi_report.json", "w"
    ) as f1, open(
        f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/raw_analysis_report.json", "w"
    ) as f2:
        json.dump(halstead_dict, f0, ensure_ascii=False, indent=2)
        json.dump(mi_dict, f1, ensure_ascii=False, indent=2)
        json.dump(raw_dict, f2, ensure_ascii=False, indent=2)


def extract_info_from_pytest(data):
    results = {}
    for line in data.strip().split('\n'):
        record = json.loads(line)
        if "nodeid" in record:
            x = record["nodeid"]
            if '::' in x:
                idx = x.find('::')
                x = x[idx + 2:]
                outcome = record["outcome"]
                duration = record["duration"]
                if x not in results:
                    if outcome == 'failed':
                        if type(record["longrepr"]) != dict:
                            results[x] = (record["outcome"], record["longrepr"], round(duration, 5))
                        else:
                            results[x] = (record["outcome"], record["longrepr"]["reprcrash"]["message"], round(duration, 5))
                    else:
                        results[x] = (record["outcome"], '', round(duration, 5))
                else:
                    if results[x][0] != outcome:
                        if outcome == 'failed':
                            if type(record["longrepr"]) != dict:
                                results.update({x: (record["outcome"], record["longrepr"], round(duration, 5))})
                            else:
                                results.update({x: (record["outcome"], record["longrepr"]["reprcrash"]["message"], round(duration, 5))})
    return results


def write_test_cases_json_report(q_no, api_name, c, params, no):
    with open(f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/test_report.json", "r") as f:
        data = f.read()
    
    results = extract_info_from_pytest(data)
    failed_tests = []
    report_dict = {"parameter(s)": params}
    for k, v in results.items():
        if v[0] == "failed":
            failed_tests.append((k, v))
        else:
            report_dict[k] = v
    
    for failed_t in failed_tests:
        report_dict[failed_t[0]] = failed_t[1]
            
    with open(f"Q{q_no}/{api_name}_results_{no}/Folder_{c}/pre_existing_test_case_report.json", "w") as f:
        json.dump(report_dict, f, ensure_ascii=False, indent=2)
        

def wrong_params_failure_reasons_writer(q_no, model, wrong_params, last_number):
    with open(
        f"Q{q_no}/{model}_results_{last_number}/wrong_params_failure_reasons.json",
        "w",
    ) as f:
        json.dump(wrong_params, f, ensure_ascii=False, indent=2)
