
def filter_chars(string):
    result = ""
    for char in string:
        if char >= ':' and char <= 'r':
            result += char
    return result
