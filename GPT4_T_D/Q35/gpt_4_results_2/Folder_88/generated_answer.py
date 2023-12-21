
def remove_repeat_chars(s):
    substring = s[4:9]
    repeat_chars = [ch for ch in substring if substring.count(ch) > 1]
    return ''.join(ch for ch in s if ch not in repeat_chars)
