def filter_chars(s):
    s = list(s)
    for i in range(43, 83):
        for j in range(i, len(s)):
            if s[j] >= ':' and s[j] <= 'Q':
                s[j] = s[i]
    return ''.join(s)
