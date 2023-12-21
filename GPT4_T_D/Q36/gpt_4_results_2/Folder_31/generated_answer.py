
def filter_chars(s):
    new_string = s
    for char in set(s[15:74]):
        if char > '9' and char < 'K':
            new_string = new_string.replace(char, '')
    return new_string
