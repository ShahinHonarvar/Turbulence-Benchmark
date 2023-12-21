
def filter_chars(string):
    return string[:155] + string[155:404].replace('(', '').replace(']', '') + string[404:]
