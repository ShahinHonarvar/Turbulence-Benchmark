
def filter_chars(s):
    chars_to_remove = set(ch for ind, ch in enumerate(s) if 61 <= ind <= 70 and '0' <= ch <= '@')
    return ''.join(ch for ch in s if ch not in chars_to_remove)
