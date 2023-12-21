
def remove_repeat_chars(s):
    s1 = s[477:709]
    repeat_chars = [char for char in s1 if s1.count(char) > 1]
    return ''.join(char for char in s if char not in repeat_chars)
