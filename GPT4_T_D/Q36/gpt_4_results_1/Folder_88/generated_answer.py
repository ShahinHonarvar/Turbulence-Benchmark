
def filter_chars(s):
    for c in s[79:81]:
        if c > 'S' and c < '[':
            s = s.replace(c, "")
    return s
