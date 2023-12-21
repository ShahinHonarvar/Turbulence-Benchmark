
def filter_chars(input_str):
    for char in input_str[35:90]:
        if 'E' <= char <= 't':
            input_str = input_str.replace(char, '')
    return input_str
