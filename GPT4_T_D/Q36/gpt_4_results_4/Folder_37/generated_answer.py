
def filter_chars(input_string):
    for i in range(45, 59):
        if '/' < input_string[i] < '6':
            input_string = input_string.replace(input_string[i], "")
    return input_string
