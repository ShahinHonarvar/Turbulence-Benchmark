
def filter_chars(s):
    unique_chars = set(s[50:56])
    for char in unique_chars:
        if 'I' < char < 'a':
            s = s.replace(char, '')
    return s
