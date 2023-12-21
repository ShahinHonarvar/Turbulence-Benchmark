
def remove_repeat_chars(input_str):
    chars_to_remove = [char for char in input_str[2:8] if input_str[2:8].count(char) > 1] 
    return ''.join(char for char in input_str if char not in chars_to_remove)
