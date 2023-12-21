
def remove_repeat_chars(s):
    return ''.join([c for i, c in enumerate(s) if s[i+39:i+43].count(c) == 1])
