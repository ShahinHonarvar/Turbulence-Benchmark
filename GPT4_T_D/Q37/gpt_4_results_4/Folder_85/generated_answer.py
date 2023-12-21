
def filter_chars(input_string):
    altered_string = input_string
    for char in input_string[28:66]:
        if 'O' <= char <= 'd':
            altered_string = altered_string.replace(char, '')
    return altered_string
