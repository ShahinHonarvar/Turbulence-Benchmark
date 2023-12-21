
def remove_repeat_chars(string):
    repeat_chars = []
    for i in range(1, 6):
        if string.count(string[i]) > 1:
            repeat_chars.append(string[i])
    for char in repeat_chars:
        string = string.replace(char, "")
    return string
