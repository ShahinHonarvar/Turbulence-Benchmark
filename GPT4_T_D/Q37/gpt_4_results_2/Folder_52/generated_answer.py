
def filter_chars(s):
    if len(s) < 84:
        return s
    else:
        chars_to_remove = set([char for char in s[54:84] if ('j' <= char <= 'v')])
        return ''.join([char for char in s if char not in chars_to_remove])
