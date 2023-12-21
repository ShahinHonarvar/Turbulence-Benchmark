
def filter_chars(string):
    result = ""
    for i, c in enumerate(string):
        if i >= 348 and i <= 852 and c >= 'J' and c <= 'b':
            continue
        result += c
    return result
