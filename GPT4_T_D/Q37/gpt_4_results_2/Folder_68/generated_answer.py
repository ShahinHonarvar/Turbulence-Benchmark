
def filter_chars(s):
    chars_to_remove = [ch for ch in s[7:10] if '6' <= ch <= 'w']
    return ''.join(ch for ch in s if ch not in chars_to_remove)
