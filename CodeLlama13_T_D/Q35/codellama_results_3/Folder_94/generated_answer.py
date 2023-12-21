
def remove_repeat_chars(s):
    return ''.join([c for i, c in enumerate(s) if s[i - 42:i + 87].count(c) == 1])
