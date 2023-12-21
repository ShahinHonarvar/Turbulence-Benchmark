
def filter_chars(input_string):
    for char in input_string[19:38]:
        if ')' < char < 'P':
            input_string = input_string.replace(char, '')
    return input_string
