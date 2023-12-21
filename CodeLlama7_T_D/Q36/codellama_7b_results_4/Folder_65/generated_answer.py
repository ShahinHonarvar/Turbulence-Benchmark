
def filter_chars(s):
    for i in range(58, 82):
        if s[i] > 'F' and s[i] < 'O':
            s = s[:i] + s[i+1:]
    return s
