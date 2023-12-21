
def remove_repeat_chars(s):
    s = list(s)
    repeat_chars = [char for char in s[33:99] if s[33:99].count(char) > 1]
    s = [char for char in s if char not in repeat_chars]
    return ''.join(s)
