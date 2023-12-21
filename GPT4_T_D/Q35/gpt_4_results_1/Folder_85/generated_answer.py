
def remove_repeat_chars(input_str):
    target_substring = input_str[2:8]
    unique_chars = set(target_substring)
    for char in unique_chars:
        if target_substring.count(char) > 1:
            input_str = input_str.replace(char, '')
    return input_str
