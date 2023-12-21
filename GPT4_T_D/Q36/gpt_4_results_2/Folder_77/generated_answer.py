
def filter_chars(s):
    chars_to_remove = {ch for ch in s[222:419] if '-' < ch < 'v'}
    result = ''.join([ch for ch in s if ch not in chars_to_remove])
    return result
