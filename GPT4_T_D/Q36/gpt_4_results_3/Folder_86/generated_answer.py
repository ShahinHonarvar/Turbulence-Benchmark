
def filter_chars(input_string):
    for char in input_string[673:709]:
        if 'X' < char < '}':
            input_string = input_string.replace(char, '')
    return input_string
