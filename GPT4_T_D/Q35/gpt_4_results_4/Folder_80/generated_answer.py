
def remove_repeat_chars(s):
    string_57_84 = s[58:84]
    for char in set(string_57_84):
        if string_57_84.count(char) > 1:
            s = s.replace(char, '')
    return s
