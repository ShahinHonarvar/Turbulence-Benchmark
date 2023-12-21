
def filter_chars(s):
    return "".join([char for char in s if (ord(char) < 92 and ord(char) > 18 and char >= '8' and char <= 'm')])
