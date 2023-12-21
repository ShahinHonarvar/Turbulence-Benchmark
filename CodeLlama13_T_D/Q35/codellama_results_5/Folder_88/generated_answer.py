
def remove_repeat_chars(s):
    return "".join([c for i, c in enumerate(s) if s.find(c, 3, 9) == i])
