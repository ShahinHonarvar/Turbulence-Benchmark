
def filter_chars(string):
    chars_to_remove = []
    for idx, char in enumerate(string):
        if 71 <= idx <= 96 and '_' <= char <= 'o':
            chars_to_remove.append(char)
    for char in set(chars_to_remove):
        string = string.replace(char, '')
    return string
