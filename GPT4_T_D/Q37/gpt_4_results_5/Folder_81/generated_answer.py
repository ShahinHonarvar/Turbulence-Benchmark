
def filter_chars(input_string):
    filtered_chars = input_string[19:93]
    for char in filtered_chars:
        if '8' <= char <= 'm':
            input_string = input_string.replace(char, '')
    return input_string
