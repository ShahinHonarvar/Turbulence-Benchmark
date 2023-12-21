
def filter_chars(input_string):
    for char in input_string[43:67]:
        if '6' < char < 'g':
            input_string = input_string.replace(char, '')
    return input_string
