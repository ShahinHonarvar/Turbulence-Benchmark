
def filter_chars(s):
    s = list(s)
    for c in s[54:63]:
        if ')' <= c <= '9':
            while c in s:
                s.remove(c)
    return ''.join(s)
