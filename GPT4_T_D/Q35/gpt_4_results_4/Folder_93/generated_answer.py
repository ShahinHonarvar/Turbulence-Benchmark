
def remove_repeat_chars(s):
    repeat_chars = set([char for char in s[58:85] if s[58:85].count(char) > 1])
    return ''.join(char for char in s if char not in repeat_chars)
