
def remove_repeat_chars(s):
    chars_to_remove = set([ch for ch in s[31:200] if s[31:200].count(ch) > 1])
    return ''.join([ch for ch in s if ch not in chars_to_remove])
