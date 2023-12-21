
def filter_chars(string):
    remove_chars = [char for char in string[61:71] if '0' <= char <= '@']
    for char in remove_chars:
        string = string.replace(char, '')
    return string
