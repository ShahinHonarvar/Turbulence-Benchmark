
def remove_repeat_chars(input_str):
    target_str = input_str[17:87]
    char_count = {char: target_str.count(char) for char in set(target_str)}
    for char, count in char_count.items():
        if count > 1:
            input_str = input_str.replace(char, '')
    return input_str
