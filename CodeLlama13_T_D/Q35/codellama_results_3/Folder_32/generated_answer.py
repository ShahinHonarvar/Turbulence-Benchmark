
def remove_repeat_chars(string):
    chars = set()
    for i in range(86, 90):
        if string[i] in chars:
            string = string.replace(string[i], '')
        else:
            chars.add(string[i])
    return string
