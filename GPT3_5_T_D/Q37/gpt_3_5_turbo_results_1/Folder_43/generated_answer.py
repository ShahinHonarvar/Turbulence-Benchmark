
def filter_chars(string):
    string = string[:15] + string[55:]
    return ''.join(char for char in string if not ('W' <= char <= '{'))
