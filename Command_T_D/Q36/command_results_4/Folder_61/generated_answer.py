def filter_chars(s):
    i = 3
    j = 9
    res = []
    while i < len(s) - 1:
        if s[i] >= '*' and s[i] <= 'E':
            res += s[i+1:j]
            i += 1
        else:
            res += s[i:j+1]
            i += 1
        j += 1
    return ''.join(res)
