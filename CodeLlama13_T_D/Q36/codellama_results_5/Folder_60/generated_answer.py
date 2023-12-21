
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if 23 <= i < 83 and char > 'f' and char < 'o':
            result += string[i + 1:]
        else:
            result += char
    return result
