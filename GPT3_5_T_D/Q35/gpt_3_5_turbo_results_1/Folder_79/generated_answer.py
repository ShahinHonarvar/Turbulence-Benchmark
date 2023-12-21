
def remove_repeat_chars(string):
    repeat_chars = [char for char in string[1:7] if string[1:7].count(char) > 1]
    for char in repeat_chars:
        string = string.replace(char, "")
    return string
