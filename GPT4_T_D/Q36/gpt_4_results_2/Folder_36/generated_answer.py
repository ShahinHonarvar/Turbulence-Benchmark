
def filter_chars(input_string):
    subset_string = input_string[284:484]
    for char in subset_string:
        if 'l' < char < 't':
            input_string = input_string.replace(char, '')
    return input_string
