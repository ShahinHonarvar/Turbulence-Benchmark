
def filter_chars(string):
    return string[:18] + ''.join([char for char in string[18:64] if char <= '3' or char >= 'B']) + string[64:]
