
def filter_chars(s):
    chars_to_remove = [ch for ch in s[67:90] if ch > '#' and ch < 'T']
    return ''.join([ch for ch in s if ch not in chars_to_remove])
