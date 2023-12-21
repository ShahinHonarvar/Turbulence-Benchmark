
def remove_repeat_chars(s):
    substring = s[40:43]
    for char in set(substring):
        if substring.count(char) > 1:
            s = s.replace(char, '')
    return s
