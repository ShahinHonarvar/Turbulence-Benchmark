
def remove_repeat_chars(string):
    repeat_chars = set()
    for i in range(33, 78):
        char = string[i]
        if char in repeat_chars:
            string = string.replace(char, "")
        else:
            repeat_chars.add(char)
    return string
