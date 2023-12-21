
def remove_repeat_chars(string):
    for char in set(string[32:44]):
        if string[32:44].count(char) > 1:
            string = string.replace(char, "")
    return string
