
def filter_chars(input_string):
    for char in input_string[64:89]:
        if '*' < char < 'w':
            input_string = input_string.replace(char, '')
    return input_string
