
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) >= 477 and ord(char) <= 984 and char >= "," and char <= "V":
            result += char
    return result
