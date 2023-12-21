
def filter_chars(input_string):
    select_chars = set(input_string[36:80])
    select_chars = [char for char in select_chars if '2' <= char <= 's']
    for char in select_chars:
        input_string = input_string.replace(char, '')
    return input_string
