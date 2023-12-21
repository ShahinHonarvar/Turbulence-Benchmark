import re
def palindromes_between_indices(text):
    text = text.lower()
    start_index = 1
    end_index = 8
    for i in range(1, end_index - 1):
        if not text[i] in text[start_index:]:
            start_index = i
            break
    for i in range(end_index, -1, -1):
        if not text[i] in text[start_index:]:
            end_index = i
            break
    return set(re.findall(r'[a-z]+', text[start_index:end_index]))
