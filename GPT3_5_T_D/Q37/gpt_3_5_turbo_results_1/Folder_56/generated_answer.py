
def filter_chars(string):
    return string[:71] + ''.join([char for char in string[71:95] if not ('K' <= char <= 'a')]) + string[95:]
