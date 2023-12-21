
def remove_repeat_chars(string):
    for char in string[72:93]:
        if string[72:93].count(char) > 1:
            string = string.replace(char, "")
    return string
