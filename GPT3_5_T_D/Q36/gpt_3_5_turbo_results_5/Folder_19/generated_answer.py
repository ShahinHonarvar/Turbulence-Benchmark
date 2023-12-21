
def filter_chars(string):
    return string[:77] + ''.join([char for char in string[77:87] if not (';' < char < 'r')]) + string[87:]
