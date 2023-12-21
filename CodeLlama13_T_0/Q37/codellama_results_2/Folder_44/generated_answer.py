
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if i < 21 or i > 43:
            result += char
        elif char >= "+" and char <= "8":
            continue
        else:
            result += char
    return result
