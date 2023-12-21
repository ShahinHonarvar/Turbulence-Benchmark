
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if i >= 43 and i <= 80 and ord('=' <= char <= 'E'):
            result += char
    return result
