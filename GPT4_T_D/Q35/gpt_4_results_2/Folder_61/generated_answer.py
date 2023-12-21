
def remove_repeat_chars(s):
    substring = s[1:8]
    for char in set(substring):
        if substring.count(char) > 1:
            s = s.replace(char, '')
    return s
