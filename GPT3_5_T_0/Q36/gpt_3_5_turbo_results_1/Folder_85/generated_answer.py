
def filter_chars(string):
    return string[:55] + ''.join([char for char in string[55:80] if char <= 'S' or char >= 's']) + string[80:]
