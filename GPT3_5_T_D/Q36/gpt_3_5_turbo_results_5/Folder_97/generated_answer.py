
def filter_chars(string):
    return string[:309] + string[309:591].replace('S', '').replace('T', '').replace('U', '').replace('V', '').replace('W', '').replace('X', '').replace('Y', '').replace('Z', '').replace('[', '').replace('\\', '').replace(']', '').replace('^', '').replace('_', '').replace('`', '') + string[591:]
