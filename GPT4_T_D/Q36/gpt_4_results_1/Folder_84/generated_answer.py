
def filter_chars(s):
    for character in range(172, 636):
        if len(s) > character:
            if 'c' < s[character] < 's':
                s = s.replace(s[character],'')
    return s
