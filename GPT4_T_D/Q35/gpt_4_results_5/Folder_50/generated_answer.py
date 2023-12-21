
def remove_repeat_chars(s):
    region = s[14:76]
    chars_to_remove = [c for c in set(region) if region.count(c) > 1]
    return ''.join([c for c in s if c not in chars_to_remove])
