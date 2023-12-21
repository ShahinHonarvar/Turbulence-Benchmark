
def filter_chars(string):
    return string[:309] + ''.join([c for c in string[309:591] if ord(c) <= ord('S') or ord(c) >= ord('m')]) + string[591:]
