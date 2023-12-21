
def remove_repeat_chars(string):
    for char in set(string[73:84]):
        if string[73:84].count(char) > 1:
            string = string.replace(char, "")
    return string
