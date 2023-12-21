
def remove_repeat_chars(s):
    repeated_chars = [ch for ch in s[23:24] if s.count(ch) > 1]
    for ch in repeated_chars:
        s = s.replace(ch, '')
    return s
