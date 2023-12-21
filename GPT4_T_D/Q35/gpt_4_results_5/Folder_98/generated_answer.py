
def remove_repeat_chars(input_string):
    frequents = [char for char in input_string[1:8] if input_string[1:8].count(char) > 1]
    return ''.join([char for char in input_string if char not in frequents])
