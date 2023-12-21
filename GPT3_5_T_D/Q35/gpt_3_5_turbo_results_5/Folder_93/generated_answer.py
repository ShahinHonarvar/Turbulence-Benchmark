
def remove_repeat_chars(string):
    for char in set(string[57:85]):
        if string[57:85].count(char) > 1:
            string = string.replace(char, "")
    return string
