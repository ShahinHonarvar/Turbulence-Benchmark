def filter_chars(s):
    for c in s[27:-2]:
        if c.isalpha() and c.lower() > 'a' and c.lower() < 'i':
            s = s.replace(c, 'z')
    return s
