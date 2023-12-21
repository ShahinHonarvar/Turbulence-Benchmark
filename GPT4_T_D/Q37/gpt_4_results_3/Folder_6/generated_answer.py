
def filter_chars(s):
    chars_to_remove = set([x for x in s[13:29] if 'c' <= x <= 'n'])
    return ''.join([ch for ch in s if ch not in chars_to_remove])
