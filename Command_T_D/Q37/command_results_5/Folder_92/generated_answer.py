def filter_chars(s):
    s = s[:4] + s[5:-4] + s[-1:]
    s = ''.join(x for x in s if x in range('7','o')))
    return s
