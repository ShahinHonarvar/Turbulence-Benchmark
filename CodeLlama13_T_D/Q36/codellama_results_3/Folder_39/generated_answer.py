
def filter_chars(string):
    result = ''
    for i, char in enumerate(string):
        if i < 43 or i > 59:
            result += char
        elif char > '5' and char < 'C':
            continue
        else:
            result += char
    return result
