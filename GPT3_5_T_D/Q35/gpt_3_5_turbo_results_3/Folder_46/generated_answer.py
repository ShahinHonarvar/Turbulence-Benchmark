
def remove_repeat_chars(string):
    for char in string:
        if 10 < string.index(char) < 79 and string.count(char) > 1:
            string = string.replace(char, "")
    return string
