
def remove_repeat_chars(string):
    for i in range(4, 9):
        char = string[i]
        if string.count(char) > 1:
            string = string.replace(char, "")
    return string
