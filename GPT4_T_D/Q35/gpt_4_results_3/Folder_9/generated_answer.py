
def remove_repeat_chars(input_string):
    if len(input_string) > 200:
        char_to_remove = [char for char in input_string[81:200] if input_string[81:200].count(char) > 1]
        result = "".join([char for char in input_string if char not in char_to_remove])
        return result
    else:
        return input_string
