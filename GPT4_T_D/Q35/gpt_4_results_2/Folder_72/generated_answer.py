
def remove_repeat_chars(s):
    to_remove = set([ch for ch in s[14:70] if s[14:70].count(ch) > 1])
    return ''.join([ch for ch in s if ch not in to_remove])
