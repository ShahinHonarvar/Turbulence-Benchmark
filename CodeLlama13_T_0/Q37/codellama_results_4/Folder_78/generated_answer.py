
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if 75 <= i <= 99 and ord('8') <= ord(char) <= ord('e'):
            continue
        result += char
    return result
