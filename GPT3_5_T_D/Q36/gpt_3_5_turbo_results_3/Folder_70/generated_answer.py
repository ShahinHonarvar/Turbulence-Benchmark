
def filter_chars(string):
    return string[:170] + ''.join([char for char in string[170:195] if char <= '!' or char >= '}']) + string[195:]
