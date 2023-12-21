
def remove_repeat_chars(string):
    for i in range(20, 200):
        if string[i] in string[:i]:
            string = string.replace(string[i], "")
    return string
