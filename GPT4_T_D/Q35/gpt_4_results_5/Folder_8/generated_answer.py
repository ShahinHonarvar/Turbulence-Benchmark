
def remove_repeat_chars(input_str):
    sub_str = input_str[46:48]
    for char in sub_str:
        if sub_str.count(char) > 1:
            input_str = input_str.replace(char, '')
    return input_str
