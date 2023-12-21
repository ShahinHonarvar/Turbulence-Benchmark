
def remove_repeat_chars(string):
    chars_to_remove = []
    for char in string[20:36]:
        if string.count(char) > 1:
            chars_to_remove.append(char)
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string
