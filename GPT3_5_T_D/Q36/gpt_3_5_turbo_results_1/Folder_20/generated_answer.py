
def filter_chars(string):
    return string[:13] + ''.join([char for char in string[13:40] if not ('Z' > char > ':' > '@' < 'C')]) + string[40:]
