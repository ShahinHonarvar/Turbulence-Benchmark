
def filter_chars(s):
    chars_to_remove = set([ch for ch in s[19:34] if 'S' <= ch <= '{'])
    return "".join([ch for ch in s if ch not in chars_to_remove])
