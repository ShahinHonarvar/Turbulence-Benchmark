
def remove_repeat_chars(string):
    for char in set(string[104:801]):
        if string.count(char) > 1:
            string = string.replace(char, "")
    return string
