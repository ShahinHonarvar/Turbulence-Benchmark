
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if i < 38 or i > 69:
            result += char
        elif char >= "H" and char <= "e":
            continue
        else:
            result += char
    return result
