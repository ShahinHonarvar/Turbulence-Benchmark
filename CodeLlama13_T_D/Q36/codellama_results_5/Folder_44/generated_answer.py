
def filter_chars(s):
    chars = []
    for i in range(18, 64):
        if s[i].isalpha() and s[i].lower() > '3' and s[i].lower() < 'b':
            chars.append(s[i])
    return "".join(chars)
