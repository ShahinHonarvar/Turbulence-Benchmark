
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) < 63 or ord(char) > 84 or (ord(char) >= 65 and ord(char) <= 90):
            result += char
    return result
