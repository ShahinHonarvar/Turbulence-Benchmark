
def filter_chars(string):
    result = ''
    for i, c in enumerate(string):
        if i >= 24 and i <= 82:
            if ord(c) >= 53 and ord(c) <= 60:
                continue
        result += c
    return result
