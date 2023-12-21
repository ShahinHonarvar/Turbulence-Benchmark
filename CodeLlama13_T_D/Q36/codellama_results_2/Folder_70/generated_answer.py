
def filter_chars(s):
    for i in range(170, 195):
        if s[i].isalnum():
            s = s.replace(s[i], '')
    return s
