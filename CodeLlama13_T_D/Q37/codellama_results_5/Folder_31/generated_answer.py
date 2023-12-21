
def filter_chars(string):
    result = ""
    for char in string:
        if (ord(char) >= 57 and ord(char) <= 96) and (ord(char) >= ord('<') and ord(char) <= ord('w')):
            continue
        else:
            result += char
    return result
