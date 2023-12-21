
def remove_repeat_chars(s):
    repeat_chars = [char for char in s[51:92] if s[51:92].count(char) > 1]
    return ''.join(ch for ch in s if ch not in repeat_chars)
