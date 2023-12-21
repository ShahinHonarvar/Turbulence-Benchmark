
def filter_chars(string):
    result = ""
    for char in string:
        if not (ord('+') <= ord(char) <= ord('}')) or len(result) < 515 or len(result) > 538:
            result += char
    return result
