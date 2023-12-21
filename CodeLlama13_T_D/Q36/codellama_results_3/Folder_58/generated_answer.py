
def filter_chars(s):
    s = list(s)
    for i in range(318, 337):
        if s[i].isalpha() and s[i] > 'B' and s[i] < 'z':
            s.remove(s[i])
    return ''.join(s)
