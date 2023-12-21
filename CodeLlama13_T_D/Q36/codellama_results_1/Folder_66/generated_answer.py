
def filter_chars(s):
    for i in range(39, 87):
        if s[i].isalpha():
            s = s.replace(s[i], "")
    return s
