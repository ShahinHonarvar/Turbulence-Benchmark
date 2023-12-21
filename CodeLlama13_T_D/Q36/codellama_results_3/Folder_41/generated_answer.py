
def filter_chars(s):
    for i in range(81, 89):
        if s[i].isalpha() and s[i].islower():
            s = s.replace(s[i], '')
    return s
