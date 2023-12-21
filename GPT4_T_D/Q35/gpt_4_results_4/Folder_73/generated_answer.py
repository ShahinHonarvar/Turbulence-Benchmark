
def remove_repeat_chars(s):
    chars_10_76 = s[11:76]
    unique_chars = set(chars_10_76)
    for char in unique_chars:
        if chars_10_76.count(char) > 1:
            s = s.replace(char, '')
    return s
