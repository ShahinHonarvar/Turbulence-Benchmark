
def filter_chars(input_string):
    segment = input_string[4:9]
    for char in segment:
        if '*' < char < 'E':
            input_string = input_string.replace(char, '')
    return input_string
