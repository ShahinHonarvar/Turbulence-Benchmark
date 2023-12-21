
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if i < 69 or i > 80:
            result += char
        elif char >= '@' and char <= 'p':
            continue
        else:
            result += char
    return result
