
def filter_chars(s):
    for i in range(25, 98):
        if s[i].lower() >= 'm' and s[i].lower() <= 'w':
            s = s[:i] + s[i+1:]
    return s
