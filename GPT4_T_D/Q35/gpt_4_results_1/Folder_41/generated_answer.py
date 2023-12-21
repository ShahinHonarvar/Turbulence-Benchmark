
def remove_repeat_chars(s):
    repeat_chars = [c for c in s[4:8] if s[4:8].count(c) > 1]
    return ''.join(char for char in s if char not in repeat_chars)
