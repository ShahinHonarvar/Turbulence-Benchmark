
def remove_repeat_chars(s):
    check_str = s[38:43]
    repeats = [c for c in check_str if check_str.count(c) > 1]
    return ''.join([c for c in s if c not in repeats])
