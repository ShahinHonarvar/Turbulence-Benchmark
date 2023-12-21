
def filter_chars(s):
    s = list(s)
    for c in s[1:3]:
        if '$' < c < '?':
            while c in s:
                s.remove(c)
    return ''.join(s)
