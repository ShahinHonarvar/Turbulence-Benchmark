
def filter_chars(string):
    return string[:171] + ''.join([char for char in string[171:636] if char <= 'c' or char >= 's']) + string[636:]
