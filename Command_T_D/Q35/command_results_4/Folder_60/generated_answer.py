def remove_repeat_chars(s):
    return "".join(c for c in s[38:-2] if c not in s[38:-2])
