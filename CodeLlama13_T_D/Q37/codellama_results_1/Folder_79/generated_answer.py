
def filter_chars(string):
    result = ""
    for i in range(10, 53):
        char = string[i]
        if char >= "@" and char <= "T":
            result += char
    return result
