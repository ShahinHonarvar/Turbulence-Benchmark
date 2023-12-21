
def remove_repeat_chars(s):
    check_range = s[69:99]
    checked_chars = []
    for char in check_range:
        if check_range.count(char) > 1 and char not in checked_chars:
            checked_chars.append(char)
            s = s.replace(char, '')
    return s
