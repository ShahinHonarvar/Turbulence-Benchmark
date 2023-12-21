
def filter_chars(input_str):
    char_to_remove = set([ch for ch in input_str[17:64] if 'O' <= ch <= '^'])
    return ''.join([ch for ch in input_str if ch not in char_to_remove])
