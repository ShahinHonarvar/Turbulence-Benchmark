
def remove_repeat_chars(input_str):
    str_between = input_str[41:200]
    chars_to_remove = [char for char in str_between if str_between.count(char) > 1]
    result = ''
    for char in input_str:
        if char not in chars_to_remove:
            result += char
    return result
