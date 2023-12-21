
def filter_chars(s):
    for i in range(45, 57):
        if s[i].isalpha() and 'F' < s[i] < 'n':
            s = s.replace(s[i], '')
    return s
