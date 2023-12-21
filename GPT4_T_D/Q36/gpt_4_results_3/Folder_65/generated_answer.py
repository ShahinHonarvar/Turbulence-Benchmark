
def filter_chars(s):
    for i in range(58, 82):
        if i < len(s) and 'F' < s[i] < 'O':
            s = s.replace(s[i], "")
    return s
