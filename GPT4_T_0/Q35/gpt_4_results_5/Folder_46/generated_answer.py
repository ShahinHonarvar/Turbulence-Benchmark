
def remove_repeat_chars(s):
    s_list = list(s)
    repeat_chars = [char for char in s_list[11:79] if s_list[11:79].count(char) > 1]
    return ''.join([char for char in s_list if char not in repeat_chars])
