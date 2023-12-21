
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) >= 164 and ord(char) <= 706 and ord(char) >= ord('O') and ord(char) <= ord('}'):
            result += char
    return result
