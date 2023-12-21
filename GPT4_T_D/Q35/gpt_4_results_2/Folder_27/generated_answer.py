
def remove_repeat_chars(s):
    chars_in_range = s[87:89]
    for char in chars_in_range:
        if chars_in_range.count(char) > 1:
            s = s.replace(char, '')
    return s
