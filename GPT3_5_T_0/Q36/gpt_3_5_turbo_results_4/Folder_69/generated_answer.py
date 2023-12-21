
def filter_chars(string):
    return string[:343] + string[343:665].replace('%', '').replace('U', '') + string[665:]
