
def filter_chars(string):
    return string[:138] + string[138:921].replace('6', '').replace('7', '').replace('8', '').replace('9', '') + string[921:]
