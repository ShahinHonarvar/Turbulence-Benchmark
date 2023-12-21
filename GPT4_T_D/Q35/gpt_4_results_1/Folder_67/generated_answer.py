
def remove_repeat_chars(s):
    repeat_chars = list(filter(lambda x: s.count(x)>1, s[45:67]))
    unique_chars = list(set(repeat_chars))
    for char in unique_chars:
        s = s.replace(char, '')
    return s
