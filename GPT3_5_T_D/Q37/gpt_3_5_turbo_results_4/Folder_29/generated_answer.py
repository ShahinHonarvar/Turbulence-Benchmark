
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if 12 <= i <= 88 and '&' <= char <= 'v':
            continue
        result += char
    return result
