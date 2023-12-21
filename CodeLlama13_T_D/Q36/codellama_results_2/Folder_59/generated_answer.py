
def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if i < 3 or i > 8:
            result.append(char)
        elif char > '?' and char < 'k':
            continue
        else:
            result.append(char)
    return "".join(result)
