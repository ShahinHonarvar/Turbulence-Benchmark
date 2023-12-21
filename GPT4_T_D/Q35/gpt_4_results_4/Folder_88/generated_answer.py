
def remove_repeat_chars(s):
    repeated_chars = set([char for char in s[4:9] if s[4:9].count(char) > 1])
    return ''.join([char for char in s if char not in repeated_chars])
