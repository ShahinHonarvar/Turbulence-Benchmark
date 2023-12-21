
def remove_repeat_chars(string):
    repeated_chars = set()
    for char in string[25:80]:
        if string.count(char) > 1:
            repeated_chars.add(char)
    for char in repeated_chars:
        string = string.replace(char, '')
    return string
