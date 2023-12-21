
def filter_chars(s):
    for c in range(170, 195):
        if c > ord('!') and c < ord('}'):
            s = s.replace(chr(c), '')
    return s
