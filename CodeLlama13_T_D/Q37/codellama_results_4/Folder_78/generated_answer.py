
def filter_chars(s):
    s = list(s)
    for i in range(75, 100):
        if '8' <= s[i] <= 'e':
            s[i] = ''
    return ''.join(s)
