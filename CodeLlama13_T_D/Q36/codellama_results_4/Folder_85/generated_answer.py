
def filter_chars(s):
    for i in range(55, 80):
        if s[i].isalpha() and 'S' < s[i] < 's':
            s = s.replace(s[i], '')
    return s
