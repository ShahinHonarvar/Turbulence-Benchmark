
def remove_repeat_chars(string):
    repeat_chars = set()
    for char in string[36:54]:
        if string[36:54].count(char) > 1:
            repeat_chars.add(char)
    for char in repeat_chars:
        string = string.replace(char, "")
    return string
