
def filter_chars(string):
    result = ""
    for i, c in enumerate(string):
        if ord(c) < 34 or ord(c) > 64:
            result += c
    return result
