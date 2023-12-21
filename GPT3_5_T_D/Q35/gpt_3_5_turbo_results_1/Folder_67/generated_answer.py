
def remove_repeat_chars(string):
    return ''.join([c for i, c in enumerate(string) if i <= 43 or i >= 67 or string[44:67].count(c) == 1])
