
def remove_repeat_chars(string):
    for char in string[2:5]:
        if string.count(char) > 1:
            string = string.replace(char, "")
    return string
