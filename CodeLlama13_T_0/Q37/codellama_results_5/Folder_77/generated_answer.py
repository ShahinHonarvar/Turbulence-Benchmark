
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) < 384 or ord(char) > 411 or (ord(char) >= ord('/') and ord(char) <= ord('8')):
            result += char
    return result
