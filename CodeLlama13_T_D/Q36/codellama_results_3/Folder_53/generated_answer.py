
def filter_chars(s):
    indices = range(90, 97)
    for i in indices:
        if s[i].isalpha() and s[i].lower() > 'j' and s[i].lower() < 'w':
            s = s.replace(s[i], '')
    return s
