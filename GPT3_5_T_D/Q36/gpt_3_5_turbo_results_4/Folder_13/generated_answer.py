
def filter_chars(s):
    return s[:323] + ''.join([c for c in s[323:526] if not ')' < c < 'O']) + s[526:]
