
def remove_repeat_chars(input_string):
    repeat_chars = [char for char in input_string[1:2] if input_string.count(char) > 1]
    return ''.join([char for char in input_string if char not in repeat_chars])
