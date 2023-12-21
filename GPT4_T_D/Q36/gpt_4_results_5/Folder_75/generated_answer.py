
def filter_chars(input_string):
    for i in input_string[47:74]:
        if '&' < i < 'M':
            input_string = input_string.replace(i, "")
    return input_string
