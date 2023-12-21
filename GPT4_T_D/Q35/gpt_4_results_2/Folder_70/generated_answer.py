
def remove_repeat_chars(s):
    sub_s = s[44:70]
    chars = [char for char in sub_s if sub_s.count(char) > 1]
    new_s = ''.join([char if char not in chars else '' for char in s])
    return new_s
