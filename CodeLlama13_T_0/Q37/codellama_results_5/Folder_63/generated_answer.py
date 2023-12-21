
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if 42 <= ord(char) <= 92 and char >= "/" and char <= "a":
            continue
        else:
            result += char
    return result
