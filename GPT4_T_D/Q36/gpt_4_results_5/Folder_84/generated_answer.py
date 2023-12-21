
def filter_chars(input_string):
    modified_chars = set([char for index, char in enumerate(input_string) if 171 < index < 636 and 'c' < char < 's'])
    for char in modified_chars:
        input_string = input_string.replace(char, '')
    return input_string
