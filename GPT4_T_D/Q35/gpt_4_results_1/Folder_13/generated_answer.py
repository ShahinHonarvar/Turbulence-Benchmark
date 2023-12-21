
def remove_repeat_chars(s):
    substring = s[47:91]
    for character in set(substring):
        if substring.count(character) > 1:
            s = s.replace(character,'')
    return s
