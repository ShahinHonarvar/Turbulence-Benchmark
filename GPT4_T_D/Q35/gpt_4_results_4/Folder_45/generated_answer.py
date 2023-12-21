
def remove_repeat_chars(s):
    s = list(s)
    repeated_chars = [char for char in s[41:200] if s[41:200].count(char) > 1]
    s = ''.join([char for char in s if char not in repeated_chars])
    return s
