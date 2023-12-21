
def remove_repeat_chars(s):
    substr = s[35:69]
    for char in substr:
        if substr.count(char) > 1:
            s = s.replace(char, '')
    return s
