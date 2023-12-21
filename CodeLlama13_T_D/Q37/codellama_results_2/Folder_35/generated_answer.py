
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) < 155 or ord(char) > 403 or (ord(char) >= 91 and ord(char) <= 93):
            continue
        else:
            result += char
    return result
