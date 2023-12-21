
def remove_repeat_chars(s):
    repeat_chars = [c for c in s[71:98] if s[71:98].count(c) > 1]
    return ''.join(c for i, c in enumerate(s) if c not in repeat_chars or s[:i].count(c) == 0)
