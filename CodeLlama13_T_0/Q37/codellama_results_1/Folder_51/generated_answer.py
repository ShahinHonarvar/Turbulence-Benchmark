
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if i < 36 or i > 40:
            result += char
        elif char >= "H" and char <= "e":
            continue
        else:
            result += char
    return result
