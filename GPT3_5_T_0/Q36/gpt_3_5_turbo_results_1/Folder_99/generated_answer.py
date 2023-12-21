
def filter_chars(string):
    return string[:476] + ''.join([char for char in string[476:948] if char <= 'b' or char >= 'd']) + string[948:]
