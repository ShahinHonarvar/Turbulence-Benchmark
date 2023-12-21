
def filter_chars(s):
    for i in range(18, 31):
        if s[i].isalnum():
            s = s.replace(s[i], '')
    return s
