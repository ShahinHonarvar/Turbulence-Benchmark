
def remove_repeat_chars(s):
    chars_between_50_and_200 = s[51:200]
    for char in set(chars_between_50_and_200):
        if chars_between_50_and_200.count(char) > 1:
            s = s.replace(char, '')
    return s
