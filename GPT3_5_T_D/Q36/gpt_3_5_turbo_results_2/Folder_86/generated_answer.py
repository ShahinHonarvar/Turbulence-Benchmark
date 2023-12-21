
def filter_chars(string):
    return string[:672] + string[672:709].replace("X", "").replace("}", "") + string[709:]
