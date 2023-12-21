
def filter_chars(s):
    filtered = ''
    for i in range(603, min(760, len(s))):
        if 'Q' <= s[i] <= 'h':
            s = s.replace(s[i], '')
    return s
