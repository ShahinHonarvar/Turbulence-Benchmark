
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) >= 43 and ord(char) <= 80:
            result += char
    return result
