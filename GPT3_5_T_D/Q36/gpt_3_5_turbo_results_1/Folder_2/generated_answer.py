
def filter_chars(string):
    return string[:421] + ''.join(char for char in string[421:854] if not 'D' < char < 'J') + string[854:]
