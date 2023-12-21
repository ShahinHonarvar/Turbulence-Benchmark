
def remove_repeat_chars(input_string):
    char_check_section = input_string[2:4]
    repeats = [char for char in char_check_section if char_check_section.count(char) > 1]
    result = ''.join([char for char in input_string if char not in repeats])
    return result
