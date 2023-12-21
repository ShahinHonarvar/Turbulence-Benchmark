
def filter_chars(string):
    return string[:4] + ''.join([char for char in string[4:8] if char <= '1' or char >= 'J']) + string[8:]
