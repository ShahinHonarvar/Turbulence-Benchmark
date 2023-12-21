
def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(37, 52):
        if s[i] in s[37:52]:
            repeat_chars.add(s[i])
    new_s = ""
    for char in s:
        if char not in repeat_chars:
            new_s += char
    return new_s
