
def remove_repeat_chars(s):
    return ''.join(c for i, c in enumerate(s) if 69 <= i < 97 or s[:i].count(c) <= 1 or s[i+1:].count(c) <= 1)
