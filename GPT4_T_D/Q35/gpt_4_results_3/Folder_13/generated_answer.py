
def remove_repeat_chars(s):
    repeat_chars = set([char for char in s[47:91] if s[47:91].count(char) > 1])
    return ''.join([c for i,c in enumerate(s) if c not in repeat_chars])
