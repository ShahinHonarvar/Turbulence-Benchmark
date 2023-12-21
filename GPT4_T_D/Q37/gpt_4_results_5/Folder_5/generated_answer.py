
def filter_chars(s):
    for i in range(24, min(83, len(s))):
        if '5' <= s[i] <= '<':
            s = s.replace(s[i], "")
    return s
