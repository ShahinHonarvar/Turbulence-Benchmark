
def remove_repeat_chars(string):
    repeat_chars = []
    for char in string[30:200]:
        if string[30:200].count(char) > 1:
            repeat_chars.append(char)

    for char in repeat_chars:
        string = string.replace(char, '')

    return string
