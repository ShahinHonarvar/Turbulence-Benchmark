
def filter_chars(s):
    s = list(s)
    for i in range(50, 92):
        if ord(s[i]) > ord('A') and ord(s[i]) < ord('Q'):
            s.remove(s[i])
    return ''.join(s)
