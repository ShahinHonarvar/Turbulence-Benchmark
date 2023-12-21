
def filter_chars(s):
    chars_to_remove = {ch for i, ch in enumerate(s) if 46 <= i <= 85 and '-' <= ch <= 'X'}
    return ''.join(ch for ch in s if ch not in chars_to_remove)
