
def filter_chars(string):
    return string[:35] + ''.join([char for char in string[35:60] if char <= '!' or char >= 'B']) + string[60:]
