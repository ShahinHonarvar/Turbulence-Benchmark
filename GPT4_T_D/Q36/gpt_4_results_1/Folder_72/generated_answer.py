
def filter_chars(input_string):
    for i in range(45, 68):
        if i < len(input_string):
            if 'W' < input_string[i] < 'x':
                input_string = input_string.replace(input_string[i], '')
    return input_string
