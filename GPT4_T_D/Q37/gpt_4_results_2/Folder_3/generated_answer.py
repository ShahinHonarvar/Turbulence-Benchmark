
def filter_chars(s):
    chars_remove = set([ch for ch in s[37:57] if '6' <= ch <= '_'])
    return ''.join([ch for ch in s if ch not in chars_remove])
