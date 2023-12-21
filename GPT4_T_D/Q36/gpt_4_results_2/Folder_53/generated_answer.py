
def filter_chars(s):
    for i in range(91, 97):
        if s[i] > 'j' and s[i] < 'w':
            s = s.replace(s[i], '')
    return s
