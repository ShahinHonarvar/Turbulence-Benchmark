
def filter_chars(string):
    result = []
    for char in string:
        if ord(char) < 49 or ord(char) > 56:
            result.append(char)
    return ''.join(result)
