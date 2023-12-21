
def filter_chars(input_string):
    for char in input_string[57:86]:
        if '+' < char < 'w':
            input_string = input_string.replace(char, '')
    return input_string
