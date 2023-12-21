
def remove_repeat_chars(string):
    return ''.join([c for i, c in enumerate(string) if (i < 0 or i >= 9 or string.count(c) == 1)])
