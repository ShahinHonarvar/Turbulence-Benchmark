
def remove_repeat_chars(input_string):
    relevant_chars = set([char for char in input_string[30:53] if input_string[30:53].count(char) > 1])
    return ''.join([char for char in input_string if char not in relevant_chars])
