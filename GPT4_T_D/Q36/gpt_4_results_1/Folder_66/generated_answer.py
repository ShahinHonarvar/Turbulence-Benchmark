
def filter_chars(s):
    for i in range(40, 87):
        if s[i] > '!' and s[i] < '}':
            s = s.replace(s[i], "")
    return s
