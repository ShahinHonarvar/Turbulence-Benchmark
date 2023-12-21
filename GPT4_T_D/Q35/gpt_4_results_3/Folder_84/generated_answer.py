
def remove_repeat_chars(str):
    sub_str = str[33:44]
    repeat_chars = [char for char in sub_str if sub_str.count(char) > 1]
    return ''.join([char for char in str if char not in repeat_chars])
