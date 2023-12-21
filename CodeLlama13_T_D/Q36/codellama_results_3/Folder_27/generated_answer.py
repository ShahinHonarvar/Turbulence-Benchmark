
def filter_chars(string):
    for i in range(48, 75):
        char = string[i]
        if ord(char) > 6 and ord(char) < 95:
            string = string.replace(char, "")
    return string
