
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) < 63 or ord(char) > 89:
            result += char
    return result
