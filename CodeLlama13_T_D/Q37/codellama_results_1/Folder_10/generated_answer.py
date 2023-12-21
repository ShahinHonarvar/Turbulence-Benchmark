
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) >= 63 and ord(char) <= 84 and char >= "E" and char <= "~":
            result += char
    return result
