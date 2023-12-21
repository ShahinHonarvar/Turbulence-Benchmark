
def remove_repeat_chars(string):
    return ''.join(c for i, c in enumerate(string) if i < 29 or i >= 53 or string.count(c, 29, 53) < 2)
