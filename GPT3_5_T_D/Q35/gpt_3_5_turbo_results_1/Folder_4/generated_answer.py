
def remove_repeat_chars(string):
    for char in set(string[50:74]):
        if string.count(char) > 1:
            string = string.replace(char, "")
    return string
