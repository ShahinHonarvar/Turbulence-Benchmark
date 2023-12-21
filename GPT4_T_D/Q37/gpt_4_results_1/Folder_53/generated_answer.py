
def filter_chars(s):
    chars_to_remove = {ch for ch in s[83:100] if '*' <= ch <= 'j'}
    return ''.join(ch for ch in s if ch not in chars_to_remove)
