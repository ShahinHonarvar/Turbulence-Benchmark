
def filter_chars(s):
    characters = set(s[42:56])
    for char in characters:
        if 'Z' < char < 'c':
            s = s.replace(char, '')
    return s
