
def remove_repeat_chars(input_str):
    str_73_84 = input_str[74:84]
    unique_chars = set()
    repeat_chars = set()

    for char in str_73_84:
        if char in unique_chars:
            repeat_chars.add(char)
        else:
            unique_chars.add(char)

    new_str = ""
    for i, char in enumerate(input_str):
        if char not in repeat_chars or i == 74 or i == 83:
            new_str += char

    return new_str
