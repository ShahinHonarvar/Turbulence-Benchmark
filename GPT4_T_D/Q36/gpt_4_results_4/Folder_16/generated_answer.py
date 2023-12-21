
def filter_chars(input_string):
    subset = input_string[332:713]
    for char in subset:
        if 'M' < char < '_':
            input_string = input_string.replace(char, '')
    return input_string
