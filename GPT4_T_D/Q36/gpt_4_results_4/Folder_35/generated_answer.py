
def filter_chars(string):
    chars_to_remove = {char for char in string[164:658] if char > '(' and char < ']'}
    return ''.join([char for char in string if char not in chars_to_remove])
