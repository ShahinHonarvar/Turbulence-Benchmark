
def remove_repeat_chars(string):
    for char in set(string[11:76]):
        if string[11:76].count(char) > 1:
            string = string.replace(char, "")
    return string
