
def remove_repeat_chars(s):
    chars = s[1:10]
    uni_chars = set(chars)

    for char in uni_chars:
        if chars.count(char) > 1:
            s = s.replace(char, '')

    return s
