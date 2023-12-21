
def remove_repeat_chars(s):
    repeat_chars = [char for char in s[21:43] if s[21:43].count(char) > 1]
    return ''.join(char for char in s if char not in repeat_chars)
