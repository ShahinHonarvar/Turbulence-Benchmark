
def filter_chars(string):
    return string[:669] + ''.join(char for char in string[669:888] if char <= 'B' or char >= 'Y') + string[888:]
