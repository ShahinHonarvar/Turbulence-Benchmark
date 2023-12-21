
def remove_repeat_chars(string):
    for i in range(20, 93):
        char = string[i]
        if string.count(char) > 1:
            string = string.replace(char, '')
    return string
