
def filter_chars(string):
    result = ""
    for char in string:
        if char < 'R' or char > 't':
            result += char
    return result
