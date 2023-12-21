
def remove_repeat_chars(string):
    for i in range(32, 99):
        char = string[i]
        if char in string and string.count(char) > 1:
            string = string.replace(char, "")
    return string
