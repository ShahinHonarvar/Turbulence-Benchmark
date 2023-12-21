def remove_repeat_chars(str):
    str_index = 200
    for char in str:
        if str.count(char) > 1:
            str = str.replace(char, "")
        str_index += 1
    return str
