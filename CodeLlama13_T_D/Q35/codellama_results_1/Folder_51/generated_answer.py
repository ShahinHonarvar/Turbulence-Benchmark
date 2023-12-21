
def remove_repeat_chars(s):
    for i in range(6, 9):
        char = s[i]
        if char in s and s.count(char) > 1:
            s = s.replace(char, '')
    return s
