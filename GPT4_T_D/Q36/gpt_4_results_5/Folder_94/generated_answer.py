
def filter_chars(s):
    subset_str = s[16:85]
    for char in subset_str:
        if 'I' < char < 'M':
            s = s.replace(char, '')
    return s
