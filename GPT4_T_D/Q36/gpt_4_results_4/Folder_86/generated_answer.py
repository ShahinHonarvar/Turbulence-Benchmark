
def filter_chars(given_string):
    chars_to_remove = [char for char in given_string[673:709] if 'X' < char < '}']
    for char in set(chars_to_remove):
        given_string = given_string.replace(char, '')
    return given_string
