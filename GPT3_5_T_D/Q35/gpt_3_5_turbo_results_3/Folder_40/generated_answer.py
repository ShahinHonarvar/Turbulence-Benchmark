
def remove_repeat_chars(string):
    for i in range(1, 3):
        char = string[i]
        if string[:i].count(char) > 1:
            string = string.replace(char, "")
    return string
