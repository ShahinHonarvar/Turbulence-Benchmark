
def remove_repeat_chars(string):
    return ''.join(c for i, c in enumerate(string) if c not in string[32:99] or string[32:99].count(c) == 1)
