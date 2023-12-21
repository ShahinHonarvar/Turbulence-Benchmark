
def remove_repeat_chars(s):
    repeat_chars = [char for char in s[7:9] if s[7:9].count(char) > 1]
    for char in repeat_chars:
        s = s.replace(char, '')
    return s
