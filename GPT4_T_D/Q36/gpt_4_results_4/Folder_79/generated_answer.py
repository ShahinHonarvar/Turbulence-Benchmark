
def filter_chars(input_string):
    preserve_chars = set(input_string[12:46])
    removal_chars = {c for c in preserve_chars if '!' < c < 'A'}
    
    for c in removal_chars:
        input_string = input_string.replace(c, '')
     
    return input_string
