
def filter_chars(string):
    result = ''
    
    for index, char in enumerate(string):
        if 35 <= index <= 40 and ')' <= char <= 'l':
            continue
        result += char
    
    return result
