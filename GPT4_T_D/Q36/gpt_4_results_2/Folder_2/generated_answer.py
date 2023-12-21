
def filter_chars(str):
    chars = set(str[422:854])
    for char in chars:
        if 'D' < char < 'J':
            str = str.replace(char, '')   
    return str
