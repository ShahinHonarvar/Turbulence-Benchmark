
def filter_chars(s):
    chars_to_remove = set(ch for ch in s[348:853] if 'J' <= ch <= 'b')
    return ''.join(ch for ch in s if ch not in chars_to_remove)
