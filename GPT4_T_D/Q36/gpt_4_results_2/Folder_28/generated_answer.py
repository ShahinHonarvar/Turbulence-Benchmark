
def filter_chars(s):
    to_remove = ""
    for i in range(32, 73):
        if s[i] > 'M' and s[i] < 'j':
            to_remove += s[i]
    for c in to_remove:
        s = s.replace(c, "")
    return s
