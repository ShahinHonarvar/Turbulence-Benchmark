
def remove_repeat_chars(s):
    repeated_chars = [char for char in s[30:53] if s[30:53].count(char) > 1]
    return ''.join([char for idx, char in enumerate(s) if char not in repeated_chars or idx < 30 or idx > 53])
