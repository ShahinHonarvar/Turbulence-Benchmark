
def remove_repeat_chars(s):
    region = s[20:32]
    for char in region:
        if region.count(char) > 1:
            s = s.replace(char, "")
    return s
