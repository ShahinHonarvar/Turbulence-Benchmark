
def remove_repeat_chars(string):
    return ''.join(c for i, c in enumerate(string) if i < 33 or i >= 78 or string.count(c) == 1)
