
def remove_repeat_chars(s):
    substring = s[58:85]
    for char in substring:
        if substring.count(char) > 1:
            s = s.replace(char, '')
    return s
