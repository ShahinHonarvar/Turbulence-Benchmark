
def filter_chars(string):
    return string[:23] + ''.join(char for char in string[23:83] if not 'f' < char < 'o') + string[83:]
