
def filter_chars(input_string):
    for char in input_string[58:69]:
        if '(' < char < 'W':
            input_string = input_string.replace(char, '')
    return input_string
