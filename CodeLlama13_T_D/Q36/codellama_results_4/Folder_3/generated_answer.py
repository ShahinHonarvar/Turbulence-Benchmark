
def filter_chars(string):
    chars = list(string)
    for i in range(42, 78):
        if chars[i] > '!' and chars[i] < '?':
            chars = [c for c in chars if c != chars[i]]
    return "".join(chars)
