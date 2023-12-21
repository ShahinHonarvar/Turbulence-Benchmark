
def filter_chars(s):
    filtered = s[114:640]
    for char in filtered:
        if '!' <= char <= 'x':
            s = s.replace(char, '')
    return s
