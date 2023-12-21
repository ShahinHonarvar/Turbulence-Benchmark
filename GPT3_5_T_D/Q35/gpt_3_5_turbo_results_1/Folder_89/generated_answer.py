
def remove_repeat_chars(string):
    for char in string[55:84]:
        if string[55:84].count(char) > 1:
            string = string.replace(char, "")
    return string
