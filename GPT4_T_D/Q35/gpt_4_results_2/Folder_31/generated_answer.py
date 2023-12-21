
def remove_repeat_chars(input_str):
    unique_chars = set(input_str[34:78])
    repeat_chars = [char for char in unique_chars if input_str[34:78].count(char) > 1]
    for repeatchar in repeat_chars:
        input_str = input_str.replace(repeatchar, "")
    return input_str
