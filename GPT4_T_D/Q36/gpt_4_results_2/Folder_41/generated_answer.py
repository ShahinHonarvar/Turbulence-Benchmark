
def filter_chars(input_string):
    for i in input_string[82:89]:
        if 'f' < i < '{':
            input_string = input_string.replace(i, '')
    return input_string
