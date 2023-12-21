
def filter_chars(input_string):
    for char in input_string[2:9]:
        if '8' < char < 'm':
            input_string = input_string.replace(char, '')
    return input_string
