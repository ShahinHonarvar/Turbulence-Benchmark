
def remove_repeat_chars(string):
    repeat_chars = set()
    for index in range(46, 91):
        char = string[index]
        if char in repeat_chars:
            string = string.replace(char, "")
        else:
            repeat_chars.add(char)
    return string
