
def remove_repeat_chars(str):
    repeat_chars = [char for char in set(str[81:200]) if str[81:200].count(char) > 1]
    return ''.join([char for char in str if char not in repeat_chars])
