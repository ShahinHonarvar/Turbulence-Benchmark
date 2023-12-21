
def filter_chars(string):
    return string[:69] + ''.join([char for char in string[69:97] if char <= 'V' or char >= 'j']) + string[97:]
