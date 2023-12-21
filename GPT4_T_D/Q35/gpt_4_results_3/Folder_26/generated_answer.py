
def remove_repeat_chars(input_string):
    relevant_chars = set(input_string[69:99])
    repet_chars = [char for char in relevant_chars if input_string[69:99].count(char) > 1]
    return ''.join(char for char in input_string if char not in repet_chars)
