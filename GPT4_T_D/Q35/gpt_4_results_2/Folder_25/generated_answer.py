
def remove_repeat_chars(s):
    repeating_chars = [c for c in s[38:43] if s[38:43].count(c) > 1]
    return ''.join([c for c in s if c not in repeating_chars])
