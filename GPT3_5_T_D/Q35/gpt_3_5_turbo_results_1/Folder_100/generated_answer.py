
def remove_repeat_chars(string):
    for i in range(44, 78):
        if string[i] in string[44:78] and string.count(string[i]) > 1:
            string = string.replace(string[i], "")
    return string
