
def remove_repeat_chars(string):
    for char_index in range(20, 51):
        char = string[char_index]
        if string.count(char) > 1:
            string = string.replace(char, "")
    return string
