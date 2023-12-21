
def remove_repeat_chars(s):
    chars = s[78:84]
    for char in chars:
        if chars.count(char) > 1:
            s = s.replace(char, '')
    return s
