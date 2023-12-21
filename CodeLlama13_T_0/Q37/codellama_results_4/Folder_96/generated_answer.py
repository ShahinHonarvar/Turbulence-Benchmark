
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) < 86 or ord(char) > 92 or ord(char) < 33 or ord(char) > 115:
            result += char
    return result
