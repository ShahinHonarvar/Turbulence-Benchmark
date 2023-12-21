
def filter_chars(string):
    return string[:45] + string[57:].replace('G', '').replace('H', '').replace('I', '').replace('J', '').replace('K', '').replace('L', '').replace('M', '') + string[57:]
