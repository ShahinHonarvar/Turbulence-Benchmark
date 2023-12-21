
def filter_chars(string):
    result = ""
    for char in string:
        if len(char) > 19 and len(char) <= 33 and ord(char) >= ord('S') and ord(char) <= ord('}'):
            result += char
    return result
