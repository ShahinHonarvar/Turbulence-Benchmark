
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if i < 41 or i > 86:
            result += char
        elif char >= "S" and char <= "s":
            continue
        else:
            result += char
    return result
