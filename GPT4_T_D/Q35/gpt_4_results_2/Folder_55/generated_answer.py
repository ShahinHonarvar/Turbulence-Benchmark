
def remove_repeat_chars(s):
    char_dict = {}
    for idx, char in enumerate(s[11:100]):
        if char in char_dict:
            s = s.replace(char, '')
        else:
            char_dict[char] = 1
    return s
