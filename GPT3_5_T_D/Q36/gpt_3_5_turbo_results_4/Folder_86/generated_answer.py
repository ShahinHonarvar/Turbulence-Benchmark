
def filter_chars(string):
    return string[:672] + ''.join([char for char in string[672:709] if char <= 'X' or char >= '}']) + string[709:]
