
def remove_repeat_chars(s):
    repeat_chars = [ch for ch in s[11:76] if s[11:76].count(ch) > 1]
    return ''.join([ch for ch in s if ch not in repeat_chars])
