
def remove_repeat_chars(string):
    for i in range(68, 99):
        char = string[i]
        if string.count(char) > 1:
            string = string.replace(char, "")
    return string
