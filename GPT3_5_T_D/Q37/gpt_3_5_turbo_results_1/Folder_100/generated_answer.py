
def filter_chars(string):
    return string[:88] + string[91:].replace('J', '').replace('K', '').replace('L', '').replace('M', '').replace('N', '').replace('O', '').replace('P', '').replace('Q', '')
