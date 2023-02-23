import os
import openai
import cohere


def cohere_query(co, query, t=0.0, f=0.0, p=0.5):
    response = co.generate(
        model='xlarge',
        prompt=query,
        max_tokens=150,
        temperature=t,
        frequency_penalty=f,
        presence_penalty=p,
        stop_sequences=["--"])

    return response.generations[0].text


def openAI_query(query):
    response = openai.Completion.create(
        model="code-davinci-002",  # code-cushman-001, code-davinci-002
        prompt=query,
        temperature=0.0,
        max_tokens=256,
        echo=True,
        presence_penalty=0.0,
        frequency_penalty=0.0)
    suggested_code = ''
    if 'choices' in response:
        if len(response['choices']) > 0:
            # print(response['choices'][0], '############')
            suggested_code = response['choices'][0]['text']
        else:
            return None
    else:
        return None

    return suggested_code


def cohere_result_trimmer(str_input):
    if 'def' not in str_input:
        return 'NoFunction'
    def_index = str_input.find('def')
    str_input_lines_list = str_input.splitlines(keepends=True)
    trimmed_str = [line[def_index - 2:] for line in str_input_lines_list]
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ#():;'
    redundant_chars = '*+>'
    for idx in range(len(trimmed_str)):
        flag = False
        current_line = trimmed_str[idx]
        for char_idx in range(len(current_line)):
            if current_line[char_idx] in redundant_chars:
                current_line = current_line[:char_idx] + ' ' + current_line[char_idx + 1:]
                flag = True
            elif current_line[char_idx] in chars:
                break
        if flag:
            trimmed_str = list(
                map(lambda x: x.replace(trimmed_str[idx], current_line),
                    trimmed_str))
    clean_str = [i for i in trimmed_str if i]
    another_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"\'()+,-.:;[]{}'
    for idx in range(len(clean_str)):
        flag = False
        current_line = clean_str[idx]
        if current_line[-1] == '\n':
            current_line = current_line[:-1]
            while True:
                if not current_line:
                    break
                if current_line[-1] in another_chars:
                    break
                elif current_line[-1] in redundant_chars:
                    current_line = current_line[:-1]
                    flag = True
            if flag:
                current_line += '\n'
                clean_str = list(
                    map(lambda x: x.replace(clean_str[idx], current_line),
                        clean_str))
    end_index = 0
    for i in range(1, len(clean_str)):
        current_element = clean_str[i]
        if not current_element.startswith(' '):
            if not current_element.startswith('\n'):
                end_index = i
                break
        elif i == len(clean_str) - 1:
            end_index = i + 1
            break
    trimmed_l = clean_str[0:end_index]

    return ''.join(trimmed_l)


def codex_result_trimmer(str_input):
    if 'def' not in str_input:
        return 'NoFunction'
    def_index = str_input.find('def')
    str_input_begins_with_def = str_input[def_index:]
    str_input_begins_with_def_list = str_input_begins_with_def.splitlines(keepends=True)
    cleaned_str_list = [line[1:] if line.startswith('+') else line for line in str_input_begins_with_def_list]
    end_index = 0
    for i in range(1, len(cleaned_str_list)):
        if not cleaned_str_list[i].startswith(' '):
            if not cleaned_str_list[i].startswith('\n'):
                end_index = i
                break
        elif i == len(cleaned_str_list) - 1:
            end_index = i + 1
            break
    trimmed_l = cleaned_str_list[0:end_index]
    return ''.join(trimmed_l)


def retrieve_model_suggestion(model, prompt):
    if model == 'Codex':
        openai.api_key = os.getenv('OPEN_AI_KEY')
        if not openai.api_key:
            print('Either the Codex api_key is not set or is not valid.')
            exit(0)
        return codex_result_trimmer(openAI_query(prompt))
    elif model == 'Cohere':
        try:
            api_key = os.getenv('COHERE_KEY')
            co = cohere.Client(api_key)
            return cohere_result_trimmer(cohere_query(co, prompt))
        except:
            print('Either the Cohere api_key is not set or is not valid.')
