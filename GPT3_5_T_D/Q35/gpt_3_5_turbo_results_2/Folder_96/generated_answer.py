
def remove_repeat_chars(string):
    repeat_chars = set()
    for i in range(60, 200):
        if string[i] in repeat_chars:
            string = string.replace(string[i], "")
        else:
            repeat_chars.add(string[i])
    return string
