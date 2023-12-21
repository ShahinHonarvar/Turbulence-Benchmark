
def remove_repeat_chars(string):
    for i in range(len(string)):
        if 86 < i < 90 and string.count(string[i]) > 1:
            string = string.replace(string[i], "")
    return string
