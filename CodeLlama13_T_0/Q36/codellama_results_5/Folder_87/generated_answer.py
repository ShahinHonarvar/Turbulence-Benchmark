
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) > 32 and ord(char) < 61:
            result += char
    return result
