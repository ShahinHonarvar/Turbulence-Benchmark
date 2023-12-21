
def filter_chars(s):
    chars_to_remove = set(ch for ch in s[75:100] if '8' <= ch <= 'e')
    return ''.join(ch for ch in s if ch not in chars_to_remove)
