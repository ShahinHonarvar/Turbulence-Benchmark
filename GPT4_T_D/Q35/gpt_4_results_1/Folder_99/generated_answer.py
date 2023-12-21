
def remove_repeat_chars(s):
    sub_s = s[451:905]
    repeated_chars = [ch for ch in set(sub_s) if sub_s.count(ch) > 1]
    for ch in repeated_chars:
        s = s.replace(ch, '')
    return s
