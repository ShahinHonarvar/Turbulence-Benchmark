
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if i < 2 or i > 6:
            result += char
        elif char >= "?" and char <= "f":
            continue
        else:
            result += char
    return result
