
def filter_chars(string):
    result = ''
    for char in string:
        if char not in range(51, 78) or ord(char) < ord('V') or ord(char) > ord('Y'):
            result += char
    return result
