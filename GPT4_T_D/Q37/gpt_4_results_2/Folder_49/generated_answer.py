
def filter_chars(input_string):
    altered_string = input_string
    for char in set(input_string[42:98]):
        if '*' <= char <= 'b':
            altered_string = altered_string.replace(char, '')
    return altered_string
