
def filter_chars(s):
    char_range = set(ch for ch in s[0:2] if '*' <= ch <= 's')
    return ''.join(ch for ch in s if ch not in char_range)
