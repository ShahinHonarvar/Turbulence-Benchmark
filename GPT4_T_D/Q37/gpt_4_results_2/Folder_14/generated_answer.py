
def filter_chars(s):
    for char in s[35:99]:
        if 'A' <= char <= 'b':
            s = s.replace(char, "")
    return s
