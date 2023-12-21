def filter_chars(s):
    i, j = 0, 0
    while i < len(s):
        if s[i] > 'j' and s[i] < 'w':
            s = s[:i] + s[j:]
            i += 1
            j += 1
        else:
            j += 1
        i += 1
    return s
