
def filter_chars(input_string):
    character_range = input_string[47:91]
    chars_to_remove = [c for c in character_range if 'D' < c < 'H']
    for char in chars_to_remove:
        input_string = input_string.replace(char, '')
    return input_string
