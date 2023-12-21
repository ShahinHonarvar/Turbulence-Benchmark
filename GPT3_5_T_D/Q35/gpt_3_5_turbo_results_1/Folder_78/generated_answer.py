
def remove_repeat_chars(string):
    return ''.join([c for i, c in enumerate(string) if (i <= 62 or i >= 96) or string.count(c, 62, 96) == 1])
