
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if i < 28 or i > 65:
            result += char
        elif char >= "O" and char <= "d":
            continue
        else:
            result += char
    return result
