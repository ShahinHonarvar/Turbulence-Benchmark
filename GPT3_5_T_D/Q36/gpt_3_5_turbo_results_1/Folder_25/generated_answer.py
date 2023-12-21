
def filter_chars(string):
    return string[:24] + string[37:].replace('A', '').replace('B', '').replace('C', '').replace('D', '').replace('E', '').replace('F', '').replace('G', '') + string[37:]
