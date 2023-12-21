def remove_repeat_chars(s):
    return ''.join(c for c in s[73:-1] if c not in s[74:-2]) + s[-1])
