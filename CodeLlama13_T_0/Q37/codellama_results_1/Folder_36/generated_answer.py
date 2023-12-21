
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) >= 259 and ord(char) <= 502 and ord(char) >= 44 and ord(char) <= 51:
            continue
        else:
            result += char
    return result
