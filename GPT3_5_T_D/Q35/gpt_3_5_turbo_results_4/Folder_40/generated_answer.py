
def remove_repeat_chars(string):
    return ''.join([c for i, c in enumerate(string) if i >= 3 or string[:3].count(c) == 1])
