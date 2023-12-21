
def filter_chars(string):
    return string[:299] + string[299:418].replace('9', '').replace(':', '').replace(';', '').replace('<', '').replace('=', '').replace('>', '').replace('?', '').replace('@', '').replace('A', '').replace('B', '').replace('C', '').replace('D', '').replace('E', '').replace('F', '').replace('G', '').replace('H', '').replace('I', '').replace('J', '').replace('K', '').replace('L', '').replace('M', '').replace('N', '').replace('O', '') + string[418:]
