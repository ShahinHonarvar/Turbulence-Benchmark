
def filter_chars(string):
    result = ""
    for char in string:
        if 7 <= ord(char) <= 8 and ord('B') <= ord(char) <= ord('H'):
            continue
        result += char
    return result
