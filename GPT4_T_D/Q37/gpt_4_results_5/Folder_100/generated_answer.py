
def filter_chars(s):
    for i in range(88, 91):
        if i < len(s) and 'J' <= s[i] <= 'Q':
            s = s.replace(s[i], '') 
    return s
