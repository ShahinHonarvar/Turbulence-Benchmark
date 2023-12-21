
def filter_chars(s):
    s = list(s)
    for i in range(32, 84):
        if ord(s[i]) > ord('m') and ord(s[i]) < ord('w'):
            s.pop(i)
    return ''.join(s)
