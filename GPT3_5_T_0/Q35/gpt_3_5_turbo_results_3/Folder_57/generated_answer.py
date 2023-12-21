
def remove_repeat_chars(string):
    for char in string[25:80]:
        if string.count(char) > 1:
            string = string.replace(char, "")
    return string
