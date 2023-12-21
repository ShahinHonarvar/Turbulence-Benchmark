
def filter_chars(string):
    removed_chars = []
    for i in range(19, 23):
        if ']' <= string[i] <= 't':
            removed_chars.append(string[i])
    for char in removed_chars:
        string = string.replace(char, '')
    return string
