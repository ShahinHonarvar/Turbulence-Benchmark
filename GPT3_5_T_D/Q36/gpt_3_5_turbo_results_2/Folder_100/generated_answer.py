
def filter_chars(string):
    return string[:43] + ''.join([char for char in string[43:69] if not 'B' < char < 'r']) + string[69:]
