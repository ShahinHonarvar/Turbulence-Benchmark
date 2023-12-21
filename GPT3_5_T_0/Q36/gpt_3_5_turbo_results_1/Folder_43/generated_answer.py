
def filter_chars(string):
    return string[:27] + string[27:75].replace('A', '').replace('B', '').replace('C', '').replace('D', '').replace('E', '').replace('F', '').replace('G', '').replace('H', '') + string[75:]
