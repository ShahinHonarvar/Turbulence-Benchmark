
def remove_repeat_chars(string):
    indices = range(91, 97)
    remove_chars = []
    for char in string:
        if 90 < ord(char) < 97 and string.count(char) > 1:
            remove_chars.append(char)
    for char in remove_chars:
        string = string.replace(char, '')
    return string
