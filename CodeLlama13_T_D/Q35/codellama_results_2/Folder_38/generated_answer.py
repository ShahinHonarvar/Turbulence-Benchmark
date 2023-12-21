
def remove_repeat_chars(string):
    chars = []
    for i in range(36, 85):
        if string[i] not in chars:
            chars.append(string[i])
        else:
            string = string.replace(string[i], "")
    return string
