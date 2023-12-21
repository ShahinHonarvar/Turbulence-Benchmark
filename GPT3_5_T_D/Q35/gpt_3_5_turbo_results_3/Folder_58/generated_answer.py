
def remove_repeat_chars(string):
    for i in range(104, 802):
        if string.count(string[i]) > 1:
            string = string.replace(string[i], "")
    return string
