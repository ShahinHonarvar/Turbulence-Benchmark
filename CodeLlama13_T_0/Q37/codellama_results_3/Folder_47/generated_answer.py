
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if 38 <= i <= 54 and ':' <= char <= 'r':
            continue
        result += char
    return result
