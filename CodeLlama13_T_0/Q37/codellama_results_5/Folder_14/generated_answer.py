
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if i < 35 or i > 98:
            result += char
        elif char >= "A" and char <= "b":
            continue
        else:
            result += char
    return result
