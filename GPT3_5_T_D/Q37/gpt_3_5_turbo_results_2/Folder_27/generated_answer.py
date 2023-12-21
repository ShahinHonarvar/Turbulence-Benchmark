
def filter_chars(string):
    return string[:43] + ''.join(char for char in string[43:81] if char < 'E' and char >= '=') + string[81:]
