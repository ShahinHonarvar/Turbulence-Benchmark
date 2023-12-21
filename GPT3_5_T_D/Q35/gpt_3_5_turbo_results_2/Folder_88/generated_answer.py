
def remove_repeat_chars(string):
    repeated_chars = [char for char in string[3:9] if string[3:9].count(char) > 1]
    for char in repeated_chars:
        string = string.replace(char, "")
    return string
