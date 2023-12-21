
def remove_repeat_chars(s):
    for i in range(13, 76):
        if s[i] != '':
            char = s[i]
            if char in s[i+1:]:
                s = s.replace(char, '')
    return s
