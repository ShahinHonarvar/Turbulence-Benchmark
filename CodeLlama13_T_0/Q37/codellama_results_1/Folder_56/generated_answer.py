
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if i < 71 or i > 94:
            result += char
        elif char >= "K" and char <= "a":
            continue
        else:
            result += char
    return result
