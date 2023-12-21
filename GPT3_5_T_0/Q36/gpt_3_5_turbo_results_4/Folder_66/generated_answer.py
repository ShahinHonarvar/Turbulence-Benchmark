
def filter_chars(string):
    return string[:39] + ''.join([char for char in string[39:87] if char <= '!' or char >= '}']) + string[87:]
