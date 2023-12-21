
def remove_repeat_chars(s):
    chars = s[36:64]
    for ch in set(chars):
        if chars.count(ch) > 1:
            s = s.replace(ch, "")
    return s
