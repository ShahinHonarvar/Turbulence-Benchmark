
def remove_repeat_chars(s):
    repeat_chars = [char for char in s[21:36] if s[21:36].count(char) > 1]
    new_s = "".join([char for char in s if char not in repeat_chars])
    return new_s
