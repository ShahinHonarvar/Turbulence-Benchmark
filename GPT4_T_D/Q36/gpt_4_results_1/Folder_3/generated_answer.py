
def filter_chars(input_string):
    for char in input_string[43:78]:
        if '!' < char < '?':
            input_string = input_string.replace(char, '')
    return input_string
