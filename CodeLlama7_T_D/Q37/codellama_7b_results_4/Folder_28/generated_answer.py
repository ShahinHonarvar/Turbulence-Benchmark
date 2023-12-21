
def filter_chars(s):
    # Remove all occurrences of characters between indices 20 and 79, both inclusive
    for i in range(20, 80):
        if s[i] >= '!' and s[i] <= 'T':
            s = s.replace(s[i], '', 1)
    return s
