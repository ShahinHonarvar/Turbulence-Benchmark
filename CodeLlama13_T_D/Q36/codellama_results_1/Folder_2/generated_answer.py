
def filter_chars(string):
    result = ""
    for char in string:
        if (ord(char) > ord('D')) and (ord(char) < ord('J')):
            result += char
    return result
