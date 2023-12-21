def remove_repeat_chars(s):
    c = {c: i for i, c in enumerate(s[36:52])}
    return ''.join(c.pop(c, None) for c in s)
