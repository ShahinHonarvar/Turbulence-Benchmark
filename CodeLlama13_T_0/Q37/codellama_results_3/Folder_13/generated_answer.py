
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) >= 9 and ord(char) <= 124:
            result += char
    return result
