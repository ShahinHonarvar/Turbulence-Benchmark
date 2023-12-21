
def remove_repeat_chars(input_string):
    s = list(input_string[38:43])
    repeating_chars = [char for char in s if s.count(char) > 1]
    result = [char for char in input_string if char not in repeating_chars]
    return "".join(result)
