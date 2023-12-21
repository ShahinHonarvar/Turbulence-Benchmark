
def filter_chars(input_string):
    
    substring = input_string[770:971]
    filter_chars = [char for char in substring if '-' <= char <= 'D']
    
    for char in set(filter_chars):
        input_string = input_string.replace(char, '')
        
    return input_string
