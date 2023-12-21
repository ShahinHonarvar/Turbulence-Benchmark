
def filter_chars(string):
    chars = list(string)
    for i in range(36, 41):
        if ord(chars[i]) >= ord('H') and ord(chars[i]) <= ord('e'):
            while chars[i] in string:
                string = string.replace(chars[i], "")
    return string
