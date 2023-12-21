
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) < 384 or ord(char) > 411 or (ord(char) >= 47 and ord(char) <= 56):
            result += char
    return result
