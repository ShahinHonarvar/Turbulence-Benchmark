
def filter_chars(string):
    result = ""
    for char in string:
        if 23 <= ord(char) <= 89 and ord('w') <= ord(char) <= ord('{'):
            continue
        else:
            result += char
    return result
