
def remove_repeat_chars(s):
    return ''.join([c for i, c in enumerate(s) if s[i:i+1].count(c) <= 1])
