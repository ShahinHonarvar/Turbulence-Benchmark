
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) >= 114 and ord(char) <= 639 and ord(char) >= 33 and ord(char) <= 120:
            result += char
    return result
