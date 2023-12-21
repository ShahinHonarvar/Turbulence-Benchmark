
def filter_chars(string):
    result = ""
    for i, c in enumerate(string):
        if i >= 722 and i <= 832 and 'K' <= c <= 'm':
            continue
        result += c
    return result
