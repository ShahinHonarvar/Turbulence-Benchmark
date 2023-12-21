
def remove_repeat_chars(string):
    string_list = list(string)
    for i in range(3, 8):
        char = string[i]
        if string.count(char) > 1:
            string = string.replace(char, "")
    return string
