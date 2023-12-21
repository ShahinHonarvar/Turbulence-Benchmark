
def filter_chars(string):
    return string[:70] + string[74:].replace('A', '').replace('B', '').replace('C', '').replace('D', '').replace('E', '') + string[74:]
