
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if 33 <= ord(char) <= 70 and ord(char) >= 7:
            continue
        else:
            result += char
    return result
