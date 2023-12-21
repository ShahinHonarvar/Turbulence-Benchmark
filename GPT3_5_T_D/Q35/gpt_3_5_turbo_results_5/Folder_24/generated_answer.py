
def remove_repeat_chars(string):
    for char in string[13:91]:
        if string[13:91].count(char) > 1:
            string = string.replace(char, "")
    return string
