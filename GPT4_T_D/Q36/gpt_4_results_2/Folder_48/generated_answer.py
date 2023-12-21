
def filter_chars(s):
    sel_chars = [x for x in s[155:222] if 'A' < x < 'f']
    for ch in sel_chars:
        s = s.replace(ch, '')
    return s
