
def filter_chars(string):
    result = ""
    for char in string:
        if char >= "*" and char <= "s":
            result += char
    return result
