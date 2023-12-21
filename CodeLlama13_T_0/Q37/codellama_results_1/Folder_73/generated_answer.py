
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if 22 <= i <= 85 and ord('7') <= ord(char) <= ord('e'):
            continue
        result += char
    return result
