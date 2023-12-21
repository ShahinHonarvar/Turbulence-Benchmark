
def remove_repeat_chars(s):
    s = list(s)
    substring = s[14:76]
    repeat_chars = [char for char in substring if substring.count(char) > 1]
    s = [char for char in s if char not in repeat_chars]
    return ''.join(s)
