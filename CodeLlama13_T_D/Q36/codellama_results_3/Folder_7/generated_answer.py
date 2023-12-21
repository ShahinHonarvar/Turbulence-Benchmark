
def filter_chars(s):
    s = list(s)
    for i in range(502, 946):
        if 'W' < s[i] < 'y':
            s[i:] = []
    return "".join(s)
