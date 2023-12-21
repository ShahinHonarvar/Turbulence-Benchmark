
def remove_repeat_chars(string):
    string = string[:36] + string[52:]
    for char in string[36:52]:
        if string.count(char) > 1:
            string = string.replace(char, "")
    return string
