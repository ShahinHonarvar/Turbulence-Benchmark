
def filter_chars(string):
    result = ''
    for i, char in enumerate(string):
        if 69 <= ord(char) <= 87 and char > '#' and char < 'L':
            continue
        result += char
    return result
