
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if i < 19 or i > 90:
            result += char
        elif char >= "F" and char <= "h":
            continue
        else:
            result += char
    return result
