
def filter_chars(input_string):
    for char in input_string[56:66]:
        if 'f' < char < '|':
            input_string = input_string.replace(char, '')
    return input_string
