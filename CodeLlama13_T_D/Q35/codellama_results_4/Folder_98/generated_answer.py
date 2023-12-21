
def remove_repeat_chars(string):
    chars = set()
    for i in range(8):
        if string[i] not in chars:
            chars.add(string[i])
    for char in chars:
        while string.count(char) > 1:
            string = string.replace(char, "")
    return string
