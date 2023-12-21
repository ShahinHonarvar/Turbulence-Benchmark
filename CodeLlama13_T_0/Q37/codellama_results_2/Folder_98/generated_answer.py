
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if i < 8 or i > 9:
            result += char
    return result
