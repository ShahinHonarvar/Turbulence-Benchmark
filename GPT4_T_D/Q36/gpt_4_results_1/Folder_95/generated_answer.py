
def filter_chars(s):
    for i in range(57, 86):
        if ord(s[i]) > ord('+') and ord(s[i]) < ord('w'):
            s = s.replace(s[i], "")
    return s
