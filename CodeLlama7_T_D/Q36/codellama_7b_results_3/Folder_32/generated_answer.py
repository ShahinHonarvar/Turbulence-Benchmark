
def filter_chars(s):
    for i in range(40, 63):
        if s[i] > '7' and s[i] < 'H':
            s = s[:i] + s[i+1:]
    return s
