
def filter_chars(string):
    return string[:11] + string[46:].replace("", "") + string[11:46].replace("", "").replace('!', '').replace('A', '') + string[46:]
