
def filter_chars(input_string):
    for char in input_string[47:74]:
        if '&' < char < 'M':
            input_string = input_string.replace(char, '')
    return input_string
