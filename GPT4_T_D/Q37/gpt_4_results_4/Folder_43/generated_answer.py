
def filter_chars(s):
    chars_to_remove = [ch for ch in s[15:56] if ch >= 'W' and ch <= '{']
    return ''.join([ch for ch in s if ch not in chars_to_remove])
