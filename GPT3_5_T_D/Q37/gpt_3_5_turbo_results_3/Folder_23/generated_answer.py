
def filter_chars(string):
    return string[:51] + string[77:].replace("V", "").replace("W", "").replace("X", "").replace("Y", "") + string[77:]
