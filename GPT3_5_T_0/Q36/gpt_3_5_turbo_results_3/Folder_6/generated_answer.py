
def filter_chars(string):
    return string[:31] + ''.join([char for char in string[31:70] if char <= 'B' or char >= 'v']) + string[70:]
