
def filter_chars(s):
    for i in range(22, min(86, len(s))):
        if '7' <= s[i] <= 'e':
            s = s.replace(s[i], "")
    return s
