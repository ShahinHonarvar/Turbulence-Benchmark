
def remove_repeat_chars(string):
    repeated_chars = set()
    for char in string[86:99]:
        if string[86:99].count(char) > 1:
            repeated_chars.add(char)
    for char in repeated_chars:
        string = string.replace(char, '')
    return string
