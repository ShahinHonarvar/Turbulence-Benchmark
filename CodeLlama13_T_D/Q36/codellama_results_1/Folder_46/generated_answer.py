
def filter_chars(s):
    s = list(s)
    for i in range(19, 69):
        if s[i] > '<' and s[i] < 'C':
            s[i] = ''
    return ''.join(s)
