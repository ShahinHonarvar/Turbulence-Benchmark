
def filter_chars(s):
    chars = list(s)
    for i in range(23, min(90, len(s))):
        if 'w' <= s[i] <= '{':
            while s[i] in chars:
                chars.remove(s[i])
    return "".join(chars)
