
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) >= 71 and ord(char) <= 94 and ord(char) >= 75 and ord(char) <= 122:
            result += char
    return result
