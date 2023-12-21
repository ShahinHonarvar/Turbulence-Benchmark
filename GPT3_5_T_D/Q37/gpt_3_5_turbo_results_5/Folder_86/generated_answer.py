
def filter_chars(string):
    return string[:164] + "".join(c for c in string[164:707] if not ('O' <= c <= '}')) + string[707:]
