
def filter_chars(s):
    filtered = ''
    for ch in s[1:8]:
        if ch < 'L' or ch > 'a':
            filtered += ch
    return s[0] + filtered + s[8:]
