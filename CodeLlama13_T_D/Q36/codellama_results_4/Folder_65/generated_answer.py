
def filter_chars(string):
    result = ''
    for i, char in enumerate(string):
        if i < 58 or i > 82:
            result += char
        elif ord(char) <= ord('F') and ord(char) >= ord('O'):
            continue
        else:
            result += char
    return result
