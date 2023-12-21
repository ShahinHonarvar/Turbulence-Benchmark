
def filter_chars(string):
    to_remove = set(string[72:93])
    result = ''
    
    for char in string:
        if char not in to_remove or char >= '<' or char <= 'J':
            result += char
            
    return result
