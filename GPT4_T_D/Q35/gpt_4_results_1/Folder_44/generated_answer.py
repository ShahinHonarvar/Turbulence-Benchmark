
def remove_repeat_chars(input_str):
    repeat_chars = [char for char in input_str[37:52] if input_str[37:52].count(char) > 1]
    return ''.join([char for char in input_str if char not in repeat_chars])
