
def filter_chars(string):
    return string[:154] + string[154:222].replace('A', '').replace('B', '').replace('C', '').replace('D', '').replace('E', '').replace('a', '').replace('b', '').replace('c', '').replace('d', '').replace('e', '') + string[222:]
