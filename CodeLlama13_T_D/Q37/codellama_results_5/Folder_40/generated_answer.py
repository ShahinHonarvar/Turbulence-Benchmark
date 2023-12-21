
def filter_chars(string):
    result = []
    for char in string:
        if char >= '*' and char <= 's':
            continue
        else:
            result.append(char)
    return ''.join(result)
