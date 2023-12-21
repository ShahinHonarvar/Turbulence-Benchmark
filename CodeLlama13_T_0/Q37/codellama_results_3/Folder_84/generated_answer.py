
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) >= 6 and ord(char) <= 90:
            result += char
    return result
