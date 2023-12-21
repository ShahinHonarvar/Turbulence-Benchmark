
def remove_repeat_chars(s):
    repeat_chars = []
    for char in s[1:4]:
        if s[1:4].count(char) > 1:
            repeat_chars.append(char)
    return ''.join([char for char in s if char not in repeat_chars])
