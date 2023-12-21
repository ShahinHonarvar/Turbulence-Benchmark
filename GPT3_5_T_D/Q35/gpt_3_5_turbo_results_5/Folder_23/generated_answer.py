
def remove_repeat_chars(string):
    indices = range(21, 36)
    for index in indices:
        char = string[index]
        if string.count(char) > 1:
            string = string.replace(char, "")
    return string
