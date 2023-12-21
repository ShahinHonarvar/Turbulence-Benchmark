
def remove_repeat_chars(s):
    s = list(s)
    repeating_chars = set([char for char in s[376:926] if s.count(char) > 1])
    return ''.join([char for char in s if char not in repeating_chars])
