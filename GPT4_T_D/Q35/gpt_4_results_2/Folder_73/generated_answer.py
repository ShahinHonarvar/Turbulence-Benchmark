
def remove_repeat_chars(s):
    repeat_chars = [char for char in s[11:76] if s[11:76].count(char) > 1]
    return ''.join([char for i, char in enumerate(s) if char not in repeat_chars or i < 11 or i > 76])
