
def remove_repeat_chars(string):
    repeated_chars = []
    for char in string[86:89]:
        if string.count(char) > 1:
            repeated_chars.append(char)
    for char in repeated_chars:
        string = string.replace(char, '')
    return string
