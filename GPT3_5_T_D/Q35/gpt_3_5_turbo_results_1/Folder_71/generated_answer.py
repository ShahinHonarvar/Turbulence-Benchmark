
def remove_repeat_chars(string):
    repeat_chars = []
    for i in range(20, 35):
        if string[i] in repeat_chars:
            repeat_chars.append(string[i])
    for char in repeat_chars:
        string = string.replace(char, "")
    return string
