
def filter_chars(string):
    chars_to_remove = [ch for ch in string[69:81] if '@' <= ch <= 'p']
    for char in set(chars_to_remove):
        string = string.replace(char, '')
    return string
