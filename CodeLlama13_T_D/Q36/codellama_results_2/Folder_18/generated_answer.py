
def filter_chars(s):
    s = list(s)
    for i in range(587, 649):
        if s[i].isalpha() and s[i] < ',' and s[i] > 'c':
            s.remove(s[i])
    return "".join(s)
