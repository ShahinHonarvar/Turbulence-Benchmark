
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) >= 477 and ord(char) <= 984 and ord(char) >= ord(',') and ord(char) <= ord('V'):
            continue
        else:
            result += char
    return result
