
def filter_chars(s):
    for i in range(323, 526):
        if s[i] > ')' and s[i] < 'O':
            s = s[:i] + s[i+1:]
    return s
