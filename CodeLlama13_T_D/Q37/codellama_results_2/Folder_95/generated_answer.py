
def filter_chars(s):
    chars = list(s)
    for i in range(35, 41):
        if ')' <= s[i] <= 'l':
            chars.remove(s[i])
    return "".join(chars)
