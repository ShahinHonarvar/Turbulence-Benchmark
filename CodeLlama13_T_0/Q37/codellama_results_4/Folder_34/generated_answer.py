
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if i < 54 or i > 62:
            result += char
        elif char >= ")" and char <= "9":
            continue
        else:
            result += char
    return result
