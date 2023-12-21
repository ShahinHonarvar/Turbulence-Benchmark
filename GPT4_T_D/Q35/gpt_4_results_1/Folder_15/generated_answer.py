
def remove_repeat_chars(s):
    unique_chars = set(s[1:4])
    return ''.join([char for char in s if s[1:4].count(char) <= 1 or char not in unique_chars])
