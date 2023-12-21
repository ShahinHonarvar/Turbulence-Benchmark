
def filter_chars(input_str):
    for i in range(27, min(86, len(input_str))):
        if 'c' <= input_str[i] <= 'i':
            input_str = input_str.replace(input_str[i], "")
    return input_str
