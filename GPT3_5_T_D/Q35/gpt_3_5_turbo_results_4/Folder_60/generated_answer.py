
def remove_repeat_chars(string):
    return "".join([c for i, c in enumerate(string) if i < 38 or i >= 52 or string.count(c) == 1])
