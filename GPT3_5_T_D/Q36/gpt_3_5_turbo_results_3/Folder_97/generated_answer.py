
def filter_chars(string):
    return string[:309] + ''.join([c for c in string[309:591] if not ('S' < c < 'm')]) + string[591:]
