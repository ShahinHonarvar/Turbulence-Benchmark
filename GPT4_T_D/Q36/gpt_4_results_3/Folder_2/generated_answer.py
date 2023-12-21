
def filter_chars(s):
    for i in range(422, 854):
        if i < len(s) and 'D' < s[i] < 'J':
            s = s.replace(s[i], '')
    return s
