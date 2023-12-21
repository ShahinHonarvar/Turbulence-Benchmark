
def remove_repeat_chars(string):
    for char in string[22:24]:
        if string.count(char) > 1:
            string = string.replace(char, "")
    return string
