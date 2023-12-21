
def filter_chars(string):
    return string[:31] + string[50:] + ''.join([char for char in string[31:50] if char <= '/' or char >= 'J'])
