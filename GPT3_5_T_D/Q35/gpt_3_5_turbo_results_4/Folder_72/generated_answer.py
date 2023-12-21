
def remove_repeat_chars(string):
    for i in range(14, 70):
        char = string[i]
        if char in string[14:70] and string.count(char) > 1:
            string = string.replace(char, "")
    return string
