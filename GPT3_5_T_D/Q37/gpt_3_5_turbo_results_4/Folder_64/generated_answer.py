
def filter_chars(string):
    return string[:1] + ''.join([char for char in string[1:7] if not ('L' <= char <= 'a')]) + string[7:]
