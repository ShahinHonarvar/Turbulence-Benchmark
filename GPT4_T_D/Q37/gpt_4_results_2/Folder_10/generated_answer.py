
def filter_chars(string):
    filtered_chars = [char for char in string[63:85] if 'E' <= char <= '~']
    for char in filtered_chars:
        string = string.replace(char, '')
    return string
