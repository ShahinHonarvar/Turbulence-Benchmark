
def filter_chars(string):
    to_remove = [char for char in string[155:222] if 'A' < char < 'f']
    for char in set(to_remove):
        string = string.replace(char, '')
    return string
