
def filter_chars(string):
    return string[:19] + ''.join([ch for ch in string[19:69] if not ('<' < ch < 'C')]) + string[69:]
