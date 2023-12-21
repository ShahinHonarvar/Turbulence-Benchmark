
def remove_repeat_chars(string):
    for char in string:
        if 13 < string.index(char) < 76 and string.count(char) > 1:
            string = string.replace(char, "")
    return string
