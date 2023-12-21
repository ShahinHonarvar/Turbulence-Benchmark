
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) >= 373 and ord(char) <= 901 and char >= "T" and char <= "h":
            continue
        else:
            result += char
    return result
