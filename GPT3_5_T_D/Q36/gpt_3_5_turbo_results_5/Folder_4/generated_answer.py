
def filter_chars(string):
    to_remove = []
    for i, char in enumerate(string):
        if 42 <= i < 67 and '6' < char < 'g':
            to_remove.append(char)
    for char in to_remove:
        string = string.replace(char, "")
    return string
