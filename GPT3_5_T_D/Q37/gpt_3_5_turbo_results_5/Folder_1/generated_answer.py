
def filter_chars(string):
    return string[:41] + ''.join(char for char in string[41:80] if not ('f' <= char <= '|')) + string[80:]
