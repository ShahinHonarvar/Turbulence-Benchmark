
def filter_chars(input_string):
    for character in input_string[39:80]:
        if '.' < character < '^':
            input_string = input_string.replace(character, '')
    return input_string
