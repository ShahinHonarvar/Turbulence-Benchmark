
def filter_chars(input_string):
    filtered_string = input_string
    for character in input_string[2:6]:
        if ',' < character < 'f':
            filtered_string = filtered_string.replace(character, '')
    return filtered_string
