
def remove_repeat_chars(string):
    return ''.join([c for i, c in enumerate(string) if i < 450 or i >= 905 or string[450:905].count(c) < 2])
