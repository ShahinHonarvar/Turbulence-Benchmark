
def remove_repeat_chars(input_string):
    substring = input_string[1:8]
    char_repeat = [char for char in substring if substring.count(char) > 1]
    return ''.join([char for char in input_string if char not in char_repeat])
