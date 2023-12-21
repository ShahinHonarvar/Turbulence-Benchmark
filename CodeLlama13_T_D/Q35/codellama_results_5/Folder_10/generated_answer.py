
def remove_repeat_chars(s):
    return ''.join([c for i, c in enumerate(s) if s[i-36:i+54].count(c) == 1])
