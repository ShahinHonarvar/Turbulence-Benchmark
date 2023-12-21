
def filter_chars(s):
    chars = list(s)
    for i in range(83, 99+1):
        if '*' <= s[i] <= 'j':
            chars[i] = ''
    return ''.join(chars)
