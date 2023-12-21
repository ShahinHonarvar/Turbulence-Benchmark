
def filter_chars(s):
    for i in range(71, 97):
        if i < len(s) and '_' <= s[i] <= 'o':
            s = s.replace(s[i], '')
    return s
