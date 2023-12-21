
def remove_repeat_chars(string):
    return ''.join([c for i, c in enumerate(string) if not (i > 61 and i < 96 and string[i+1:].count(c) > 0)])
