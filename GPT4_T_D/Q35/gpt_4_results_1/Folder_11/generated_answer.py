
def remove_repeat_chars(input_string):
    str_between_indices = input_string[49:76]
    repeat_chars = [char for char in str_between_indices if str_between_indices.count(char) > 1]
    output_string = "".join([char for char in input_string if char not in repeat_chars])
    return output_string
