
def remove_repeat_chars(string):
    for i in range(72, 93):
        if string[i] in string[i+1:93]:
            string = string.replace(string[i], "")
    return string
