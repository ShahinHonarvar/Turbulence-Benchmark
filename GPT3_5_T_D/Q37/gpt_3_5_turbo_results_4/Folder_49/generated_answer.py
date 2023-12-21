
def filter_chars(string):
    return ''.join(char for char in string if not (42 <= ord(char) <= 97 and '*' <= char <= 'b'))
