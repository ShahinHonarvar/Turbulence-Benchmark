
def filter_chars(input_string):
    chars_to_remove = set([char for char in input_string[345:874] if 'f' < char < '~'])
    for char in chars_to_remove:
        input_string = input_string.replace(char, '')
    return input_string
