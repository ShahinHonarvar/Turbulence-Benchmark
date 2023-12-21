
def filter_chars(string):
    chars_to_remove = []
    for char in string[11:46]:
        if '!' < char < 'A':
            chars_to_remove.append(char)
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string
