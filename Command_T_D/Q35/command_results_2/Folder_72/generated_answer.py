def remove_repeat_chars(s):
    return ''.join(c for c in s[13:-70] if c not in s[13:-70] * 2)
