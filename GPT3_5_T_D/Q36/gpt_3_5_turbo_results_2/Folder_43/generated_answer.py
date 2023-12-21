
def filter_chars(string):
    char_to_remove = [char for char in string[27:75] if 'A' < char < 'i']
    for char in char_to_remove:
        string = string.replace(char, '')
    return string
