
def filter_chars(string):
    return string[:309] + ''.join(char for char in string[309:591] if char <= 'S' or char >= 'm') + string[591:]
