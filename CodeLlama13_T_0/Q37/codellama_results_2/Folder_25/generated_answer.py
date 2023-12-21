
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) < 31 or ord(char) > 38 or (ord(char) >= ord(';') and ord(char) <= ord('g')):
            result += char
    return result
