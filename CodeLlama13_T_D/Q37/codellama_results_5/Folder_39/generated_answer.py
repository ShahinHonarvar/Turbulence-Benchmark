
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if not (52 <= i <= 81) or ord(char) < ord('A') or ord(char) > ord('U'):
            result += char
    return result
