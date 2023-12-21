
def remove_repeat_chars(string):
    repeat_chars = []
    for i in range(38, 52):
        if string[i] not in repeat_chars and string.count(string[i], 38, 52) > 1:
            repeat_chars.append(string[i])
    for char in repeat_chars:
        string = string.replace(char, "")
    return string
