
def filter_chars(string):
    result = ""
    for i, c in enumerate(string):
        if i < 45 or i > 57:
            result += c
        elif c > "F" and c < "n":
            continue
        else:
            result += c
    return result
