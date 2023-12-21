
def remove_repeat_chars(s):
    test_range = s[2:4]
    for char in test_range:
        if test_range.count(char) > 1:
            s = s.replace(char, '')
    return s
