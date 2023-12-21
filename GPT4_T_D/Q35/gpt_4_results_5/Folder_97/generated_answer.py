
def remove_repeat_chars(input_string):
    repeat_chars = set([char for char in input_string[35:69] if input_string[35:69].count(char) > 1])
    return ''.join([char for char in input_string if char not in repeat_chars])
