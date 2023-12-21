
def remove_repeat_chars(s):
    chars = s[1:7]
    unique_chars = set(chars)
    for char in unique_chars:
        if chars.count(char) > 1:
            s = s.replace(char, '')
    return s
