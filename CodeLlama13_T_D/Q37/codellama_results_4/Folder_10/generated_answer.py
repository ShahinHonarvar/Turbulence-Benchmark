
def filter_chars(s):
    for i in range(63, 85):
        if ord(s[i]) >= ord('E') and ord(s[i]) <= ord('~'):
            s = s.replace(s[i], '')
    return s
