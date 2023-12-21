
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if i < 13 or i > 28:
            result += char
        elif char >= "c" and char <= "n":
            continue
        else:
            result += char
    return result
