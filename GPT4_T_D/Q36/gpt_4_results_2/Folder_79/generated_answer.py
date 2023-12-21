
def filter_chars(input_string):
    for character in input_string[12:46]:
        if '!' < character < 'A':
            input_string = input_string.replace(character, '')
    return input_string
