
def filter_chars(input_str):
    for char in input_str[12:78]:
        if ':' <= char <= 'L':
            input_str = input_str.replace(char, '')
    return input_str
