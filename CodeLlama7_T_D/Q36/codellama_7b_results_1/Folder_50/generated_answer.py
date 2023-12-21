
def filter_chars(s):
    for i in range(61, 88):
        if s[i] > '%' and s[i] < 'q':
            s = s[:i] + s[i+1:]
    return s
