
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) < 46 or ord(char) > 91:
            result += char
    return result
