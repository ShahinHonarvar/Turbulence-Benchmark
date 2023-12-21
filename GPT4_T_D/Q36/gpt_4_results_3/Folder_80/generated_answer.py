
def filter_chars(s):
    for i in range(55, 92):
        if i < len(s) and 'J' < s[i] < 'X':
            s = s.replace(s[i], "")
    return s
