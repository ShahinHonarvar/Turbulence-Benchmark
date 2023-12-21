
def remove_repeat_chars(s):
    repeat_chars = set()
    for char in s[81:200]:
        if s[81:200].count(char) > 1:
            repeat_chars.add(char)
    for char in repeat_chars:
        s = s.replace(char, "")
    return s
