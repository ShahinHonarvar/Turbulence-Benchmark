
def remove_repeat_chars(s):
    return "".join([c for i, c in enumerate(s) if i < 1 or i >= 8 or s.count(c, 1, 8) <= 1])
