
def remove_repeat_chars(s):
    char_to_remove = set([char for char in s[21:200] if s[21:200].count(char) > 1])
    return ''.join([char for char in s if char not in char_to_remove])
