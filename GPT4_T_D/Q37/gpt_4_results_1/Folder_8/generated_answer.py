
def filter_chars(input_str):
    for char in set(input_str[41:87]):
        if 'S' <= char <= 's':
            input_str = input_str.replace(char, '')
    return input_str
