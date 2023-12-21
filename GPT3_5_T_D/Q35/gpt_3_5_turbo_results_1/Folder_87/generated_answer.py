
def remove_repeat_chars(string):
    for char in set(string[20:43]):
        if string.count(char) > 1:
            string = string.replace(char, "")
    return string
