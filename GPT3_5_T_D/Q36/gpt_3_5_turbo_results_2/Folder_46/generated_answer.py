
def filter_chars(string):
    return string[:19] + string[19:69].replace('<', '').replace('>', '') + string[69:]
