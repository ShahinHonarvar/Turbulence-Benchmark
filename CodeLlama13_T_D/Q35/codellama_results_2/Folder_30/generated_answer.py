
def remove_repeat_chars(string):
    for i in range(22, 24):
        if string[i] in string and string.count(string[i]) > 1:
            string = string.replace(string[i], "")
    return string
