
def filter_chars(s):
    chars_to_remove = set(i for i in s[15:56] if 'W' <= i <= '{')
    return ''.join(i for i in s if i not in chars_to_remove)
