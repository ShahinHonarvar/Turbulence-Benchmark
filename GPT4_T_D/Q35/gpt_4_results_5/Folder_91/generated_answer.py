
def remove_repeat_chars(s):
    repeat_chars = [char for char in s[1:6] if s[1:6].count(char) > 1]
    return ''.join(c for c in s if c not in repeat_chars)
