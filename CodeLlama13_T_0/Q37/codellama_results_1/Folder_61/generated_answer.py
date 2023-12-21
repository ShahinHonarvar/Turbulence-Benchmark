
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if i < 5 or i > 6:
            result += char
        elif char >= "G" and char <= "p":
            continue
        else:
            result += char
    return result
