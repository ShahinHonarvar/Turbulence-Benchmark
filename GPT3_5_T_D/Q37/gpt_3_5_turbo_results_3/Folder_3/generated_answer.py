
def filter_chars(string):
    return string[:37] + string[37:57].replace('6', '').replace('7', '') + string[57:]
