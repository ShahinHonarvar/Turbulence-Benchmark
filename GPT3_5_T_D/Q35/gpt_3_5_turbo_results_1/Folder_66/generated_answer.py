
def remove_repeat_chars(string):
    indices = range(12, 76)
    for i in indices:
        char = string[i]
        if string.count(char) > 1:
            string = string.replace(char, "")
    return string
