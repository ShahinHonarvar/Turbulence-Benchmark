
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if i < 19 or i > 33:
            result += char
        elif char >= "S" and char <= "{":
            continue
        else:
            result += char
    return result
