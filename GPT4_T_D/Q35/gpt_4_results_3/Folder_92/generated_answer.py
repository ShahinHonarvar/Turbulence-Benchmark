
def remove_repeat_chars(s):
    checked_chars = []
    for char in s[1:3]:
        if char not in checked_chars:
            checked_chars.append(char)
        else:
            s = s.replace(char, '')      
    return s
