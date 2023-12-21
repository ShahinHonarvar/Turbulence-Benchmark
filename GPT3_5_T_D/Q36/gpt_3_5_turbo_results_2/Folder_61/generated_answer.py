
def filter_chars(string):
    return string[:3] + ''.join(char for char in string[3:9] if char <= '*' or char >= 'E') + string[9:]
