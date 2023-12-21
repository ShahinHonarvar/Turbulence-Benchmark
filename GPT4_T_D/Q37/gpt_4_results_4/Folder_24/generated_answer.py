
def filter_chars(input_string):
    filtered_chars = input_string[36:80]
    for char in filtered_chars:
        if '2' <= char <= 's':
            input_string = input_string.replace(char, '')
    return input_string
