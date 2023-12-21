
def remove_repeat_chars(s):
    repeat_chars = [char for char in s[14:70] if s[14:70].count(char) > 1]
    new_s = "".join(char for char in s if char not in repeat_chars)
    return new_s
