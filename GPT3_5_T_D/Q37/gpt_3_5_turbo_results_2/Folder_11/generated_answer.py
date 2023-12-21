
def filter_chars(string):
    return ''.join(char for char in string if not(29 <= ord(char) <= 97 and '-' <= char <= 'n'))
