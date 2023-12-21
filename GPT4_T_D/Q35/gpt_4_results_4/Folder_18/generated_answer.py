
def remove_repeat_chars(s):
    repeats = set()
    for char in s[57:90]:
        if s[57:90].count(char) > 1:
            repeats.add(char)
    for char in repeats:
        s = s.replace(char, '')
    return s
