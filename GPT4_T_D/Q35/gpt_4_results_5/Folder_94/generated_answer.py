
def remove_repeat_chars(input_string):
    target_substring = input_string[43:87]
    to_remove = set([char for char in target_substring if target_substring.count(char) > 1])
    result_string = "".join([char for char in input_string if char not in to_remove])
    return result_string
