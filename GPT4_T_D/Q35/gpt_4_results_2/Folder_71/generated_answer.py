
def remove_repeat_chars(s):
    sub_string = s[21:35]
    for character in set(sub_string):
        if sub_string.count(character) > 1:
            s = s.replace(character, '')
    return s
