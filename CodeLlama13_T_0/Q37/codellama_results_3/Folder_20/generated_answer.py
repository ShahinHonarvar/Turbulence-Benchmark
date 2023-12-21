
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) >= 109 and ord(char) <= 122:
            result += char
    return result
