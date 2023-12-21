
def remove_repeat_chars(string):
    chars_2_7 = set(string[3:7])
    repeat_chars = [char for char in chars_2_7 if string.count(char) > 1]
    for char in repeat_chars:
        string = string.replace(char, "")
    return string
