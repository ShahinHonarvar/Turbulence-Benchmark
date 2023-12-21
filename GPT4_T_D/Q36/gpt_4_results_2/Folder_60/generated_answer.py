
def filter_chars(input_string):
    for char in input_string[24:83]:
        if 'f' < char < 'o':
            input_string = input_string.replace(char, '')
    return input_string
