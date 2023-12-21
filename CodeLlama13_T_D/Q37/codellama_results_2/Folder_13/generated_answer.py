
def filter_chars(string):
    result = ""
    for char in string:
        if (124 <= ord(char) <= 854 and char >= '9' and char <= 's'):
            continue
        result += char
    return result
