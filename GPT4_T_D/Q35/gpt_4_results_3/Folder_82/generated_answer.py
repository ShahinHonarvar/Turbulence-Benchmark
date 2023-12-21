
def remove_repeat_chars(s):
    chars = set()
    for char in s[31:200]:
        if s[31:200].count(char) > 1:
            chars.add(char)
    for char in chars:
        s = s.replace(char, '')
    return s
