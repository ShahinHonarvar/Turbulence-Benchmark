
def remove_repeat_chars(string):
    repeat_chars = []
    for char in string[32:44]:
        if string.count(char) > 1:
            repeat_chars.append(char)

    for char in repeat_chars:
        string = string.replace(char, "")

    return string
