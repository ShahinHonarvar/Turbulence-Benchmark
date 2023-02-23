from typing import List
from os.path import exists


def file_parser(file_input='input.txt'):
    dict_q_a = {}
    if exists(file_input):
        with open(file_input, 'r') as f:
            lines = list(f)
            chunks = split_input_file_into_chunks_of_q_a(lines)
            for chunk in chunks:
                question, answer = split_question_answer(chunk)
                dict_q_a[question] = answer

    return dict_q_a


def split_input_file_into_chunks_of_q_a(lines: List[str]):
    chunks = []
    chunk = ''
    for i in range(len(lines)):
        if lines[i].startswith('#('):
            if i == 0:
                chunk += lines[i]
            else:
                chunks.append(chunk)
                chunk = ''
                chunk += lines[i]
        else:
            chunk += lines[i]
    chunks.append(chunk)

    return chunks


def split_question_answer(chunk: str):
    def_idx = chunk.index('def')
    question = chunk[0:def_idx]
    trimmed_question = line_trimmer(question)
    answer = chunk[def_idx:]

    return ''.join(trimmed_question), ''.join(answer)


def line_trimmer(line: str):
    index_ = line.find('A')
    return line[index_:]
