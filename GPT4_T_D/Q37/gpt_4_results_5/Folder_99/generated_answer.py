
def filter_chars(input_string):
    chars_to_remove = [char for char in input_string[373:902] if 'T' <= char <= 'h']
    for char in chars_to_remove:
        input_string = input_string.replace(char, '')
    return input_string
