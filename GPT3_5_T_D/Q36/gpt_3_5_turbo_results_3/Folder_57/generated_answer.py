
def filter_chars(string):
    char_to_remove = string[70:74]
    filtered_string = ''.join([char for char in string if char not in char_to_remove or char < 'A' or char >= 'U'])
    return filtered_string
