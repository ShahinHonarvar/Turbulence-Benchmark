
def filter_chars(s):
    for char in s[4:8]:
        if '?' < char < 'k':
            s = s.replace(char, '')
    return s
