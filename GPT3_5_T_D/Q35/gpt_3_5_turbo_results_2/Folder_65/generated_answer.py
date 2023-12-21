
def remove_repeat_chars(string):
    for i in range(51, 76):
        char = string[i]
        count = string.count(char)
        if count > 1:
            string = string.replace(char, "")
    return string
