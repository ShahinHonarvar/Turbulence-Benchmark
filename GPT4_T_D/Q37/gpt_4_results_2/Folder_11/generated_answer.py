
def filter_chars(s):
    chars_to_remove = set(ch for i, ch in enumerate(s) if 29 <= i <= 97 and '-' <= ch <= 'n')
    return ''.join(ch for ch in s if ch not in chars_to_remove)
