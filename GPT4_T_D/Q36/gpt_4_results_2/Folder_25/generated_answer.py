
def filter_chars(input_string):
    for char in input_string[25:37]:
        if 'A' < char < 'h':
            input_string = input_string.replace(char, '')
    return input_string
