
def remove_repeat_chars(s):
    repeat_chars = set([char for char in s[463:995] if s[463:995].count(char) > 1])
    return ''.join([char for char in s if char not in repeat_chars])
