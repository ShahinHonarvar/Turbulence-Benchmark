
def filter_chars(string):
    chars = string[11:33]
    filtered_chars = ''.join([char for char in chars if not ('!' <= char <= '@')])
    return string.replace(chars, filtered_chars)
