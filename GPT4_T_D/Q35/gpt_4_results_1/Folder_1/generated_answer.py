
def remove_repeat_chars(s):
    repeat_chars = [ch for ch in s[18:88] if s[18:88].count(ch) > 1]
    return ''.join(ch for ch in s if ch not in repeat_chars)
