
def filter_chars(string):
    return string[:11] + string[11:33].replace('!', '').replace('@', '') + string[33:]
