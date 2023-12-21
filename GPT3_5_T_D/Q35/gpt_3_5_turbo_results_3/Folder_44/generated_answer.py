
def remove_repeat_chars(string):
    chars_to_remove = set()
    for char in string[36:52]:
        if string.count(char) > 1:
            chars_to_remove.add(char)

    for char in chars_to_remove:
        string = string.replace(char, '')

    return string
