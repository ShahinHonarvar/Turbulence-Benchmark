
def remove_repeat_chars(s):
    to_remove = [c for c in s[36:64] if s[36:64].count(c) > 1]
    return ''.join(c for c in s if c not in to_remove)
