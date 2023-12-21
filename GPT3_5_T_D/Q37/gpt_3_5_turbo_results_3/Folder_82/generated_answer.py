
def filter_chars(string):
    return string[:12] + string[12:26].replace('P', '').replace('Q', '').replace('R', '').replace('S', '').replace('T', '').replace('U', '').replace('V', '').replace('W', '').replace('X', '') + string[26:]
