
def remove_repeat_chars(s):
    repeated_chars = [char for char in s[35:69] if s[35:69].count(char) > 1]
    return ''.join(char for char in s if char not in repeated_chars)
