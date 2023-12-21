
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if 36 <= ord(char) <= 79 and 'a' <= char <= 'i':
            continue
        result += char
    return result
