import re
import difflib
import itertools
from file_parser import file_parser
from generator import input_generator
from model_connection import retrieve_model_suggestion


def extract_common_layout(correct_answers):
    functions_list = []
    for k, v in correct_answers.items():
        functions_list.append(v[1])

    functions_pairs = list(itertools.combinations(functions_list, 2))
    functions_list = []
    for i in functions_pairs:
        diff = difflib.Differ()
        comparison = list(diff.compare(i[0], i[1]))
        similarity = [st[2:] if not st.startswith('+') and not st.startswith('-') else '' for st in comparison]
        functions_list.append(''.join(similarity))

    functions_pairs = list(itertools.combinations(functions_list, 2))
    result = []
    if len(functions_list) > 1:
        for i in functions_pairs:
            diff = difflib.Differ()
            comparison = list(diff.compare(i[0], i[1]))
            similarity = [st[2:] if not st.startswith('+') and not st.startswith('-') else '' for st in comparison]
            result.append(''.join(similarity))
        return set(result)

    return set(functions_list)


def run_model_answer(function: str, is_model_code: bool, generated_inputs):
    d = {}
    if is_model_code:
        first_idx = function.find('(')
        end_idx = function.find(')')
        if end_idx - first_idx > 1:
            parameters = function[first_idx + 1: end_idx].replace(' ', '').split(",")
            values = list(generated_inputs.values())
            function = function[:first_idx + 1] + function[end_idx:]
            for i in range(len(parameters)):
                function = re.sub(r'\b' + parameters[i] + r'\b', str(values[i]), function)

    if 'print' in function:
        new_function = function.replace('print', 'yield')
        try:
            exec(new_function, globals(), d)
            b, = d.values()
            return [i for i in b()]
        except:
            return 'Exception'
    try:
        exec(function, globals(), d)
        b, = d.values()
        if 'yield' in function:
            return [i for i in b()]

        return b()
    except:
        return 'Exception'


def prepare_q_a(model='Codex', number_of_tests=1):

    dict_q_a = file_parser()
    counter_examples = {}
    correct_answers = {}
    for question, answer in dict_q_a.items():
        first_idx = answer.find('(')
        end_idx = answer.find(')')
        trimmed_answer = answer[:first_idx + 1] + answer[end_idx:]
        for _ in range(number_of_tests):
            question_with_input, var_inputs = fill_question_with_input(question)
            model_code = retrieve_model_suggestion(model, question_with_input)
            function_with_input = fill_function_with_input(trimmed_answer, var_inputs)
            model_answer_output = run_model_answer(function_with_input, False, _)
            if model_code != 'NoFunction' and model_code != 'Exception':
                codex_code_output = run_model_answer(model_code, True, var_inputs)
                values = [var_inputs, model_code, codex_code_output, model_answer_output]
                if codex_code_output != model_answer_output:
                    counter_examples[question_with_input] = values
                else:
                    correct_answers[question_with_input] = values
            else:
                counter_examples[question_with_input] = [var_inputs, model_code, '',
                                                         model_answer_output]
        break
    return correct_answers, counter_examples


def fill_function_with_input(answer, var_inputs):
    answer_with_input = ''
    keys = list(var_inputs.keys())
    for key_idx in range(len(keys)):
        key = keys[key_idx]
        if key_idx == 0:
            answer_with_input = answer.replace(str(key), str(var_inputs.get(key)))
        else:
            answer_with_input = answer_with_input.replace(str(key), str(var_inputs.get(key)))

    return answer_with_input


def fill_question_with_input(question):
    holes = hole_detector(question)
    information = info_detector(holes)
    if has_duplicates(information):
        information = remove_duplicates(information)
    var_inputs = {}
    c = 0
    for info in information:
        var_ = info[0]
        if 'samesize' in info:
            if 'H0' in var_inputs:
                size = len(var_inputs.get('H0'))
                var_inputs[var_] = input_generator(info, c, size)
            else:
                var_inputs[var_] = input_generator(info, c, -1)
        else:
            var_inputs[var_] = input_generator(info, c, -2)
        if 'int' in info:
            c += 1
    question_with_input = ''
    for h_idx in range(len(holes)):
        if h_idx == 0:
            question_with_input = question.replace(holes[h_idx], str(var_inputs.get(holes[h_idx][1:3])))
        else:
            question_with_input = question_with_input.replace(holes[h_idx],
                                                              str(var_inputs.get(holes[h_idx][1:3])))

    return question_with_input, var_inputs


def has_duplicates(ls):
    if not ls:
        return False
    first_e = ls[0]
    ls = ls[1:]
    if first_e in ls:
        return True
    else:
        return has_duplicates(ls)


def remove_duplicates(ls):
    result = []
    for i in ls:
        if i not in result:
            result.append(i)
    return result


def hole_detector(line: str):
    holes = []
    words = line.split()
    for w in words:
        if w.startswith('{'):
            end_idx = w.find('}')
            w = w[:end_idx + 1]
            holes.append(w)
    return holes


def info_detector(holes):
    result = []
    for h in holes:
        data_structure = ''
        type_ = ''
        requirement = ''
        r = []
        comma_index = h.find(',')
        var = h[1:comma_index]
        r.append(var)
        h = h[comma_index + 1:]
        if h[0] == 'S':
            comma_index = h.find(',')
            data_structure = h[2:comma_index]
            h = h[comma_index + 1:]
        r.append(data_structure)
        if h[0] == 'T':
            if 'R' in h:
                comma_index = h.find(',')
                type_ = h[2:comma_index]
                h = h[comma_index + 1:]
                requirement = h[2:len(h) - 1]
            else:
                type_ = h[2:len(h) - 1]

        r.append(type_)
        r.append(requirement)
        result.append(r)
    return result
