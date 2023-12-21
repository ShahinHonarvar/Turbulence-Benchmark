
def remove_repeat_chars(s):
    chars_occur = []
    for i in range(1, 11):
        char = s[i]
        if s.count(char) > 1:
            chars_occur.append(char)

    for char in set(chars_occur):
        s = s.replace(char, '')
    
    return s
