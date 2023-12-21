
def filter_chars(arg_string):
    filtered_chars = arg_string[36:41]

    for char in filtered_chars:
        if 'H' <= char <= 'e':
            arg_string = arg_string.replace(char, '')

    return arg_string
