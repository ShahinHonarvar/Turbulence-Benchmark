
def filter_chars(s):
    char_set = set([char for char in s[43:67] if '6' < char < 'g'])
    for char in char_set:
        s = s.replace(char, '')
    return s
