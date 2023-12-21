
def filter_chars(input_string):
    substring = input_string[300:418]
    for character in substring:
        if '9' < character < 'P':
            input_string = input_string.replace(character, '')
    return input_string
