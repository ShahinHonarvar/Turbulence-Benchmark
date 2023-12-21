
def filter_chars(s):
    s = list(s)
    for i in range(78, 81):
        if s[i].isalpha() and s[i] > 'S' and s[i] < '[':
            s.remove(s[i])
    return ''.join(s)
