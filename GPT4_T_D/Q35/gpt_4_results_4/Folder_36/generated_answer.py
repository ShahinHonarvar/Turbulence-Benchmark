
def remove_repeat_chars(s):
    repeat_chars = set([char for char in s[477:709] if s[477:709].count(char) > 1])
    return ''.join([char for char in s if char not in repeat_chars])
