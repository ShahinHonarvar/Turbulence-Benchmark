
def filter_chars(string):
    chars_to_remove = [c for c in string[86:93] if '!' <= c <= 's']
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string
