
def remove_repeat_chars(string):
    for char in string[16:87]:
        if string.count(char) > 1:
            string = string.replace(char, "")
    return string
