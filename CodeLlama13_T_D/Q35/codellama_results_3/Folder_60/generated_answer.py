
def remove_repeat_chars(s):
    chars = set()
    for i in range(38, 52):
        if s[i] in chars:
            s = s[:i] + s[i+1:]
        else:
            chars.add(s[i])
    return s
