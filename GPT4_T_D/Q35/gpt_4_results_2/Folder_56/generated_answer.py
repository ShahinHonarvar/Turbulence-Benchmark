
def remove_repeat_chars(s):
    repeat_chars = [char for char in s[8:9] if s[8:9].count(char) > 1]
    return ''.join(['' if char in repeat_chars else char for char in s])
