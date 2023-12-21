
def filter_chars(s):
    for ch in s[55:92]:
        if 'J' < ch < 'X':
            s = s.replace(ch, "")
    return s
