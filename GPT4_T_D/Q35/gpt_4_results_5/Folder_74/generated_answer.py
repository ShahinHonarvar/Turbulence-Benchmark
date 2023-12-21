
def remove_repeat_chars(s):
    repeated_chars = set([ch for ch in s[70:97] if s[70:97].count(ch) > 1])
    return ''.join(ch for ch in s if ch not in repeated_chars)
