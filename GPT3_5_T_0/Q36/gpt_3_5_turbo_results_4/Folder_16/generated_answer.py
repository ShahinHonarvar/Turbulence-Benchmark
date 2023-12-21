
def filter_chars(string):
    return string[:331] + ''.join([char for char in string[331:713] if char <= 'M' or char >= '_']) + string[713:]
