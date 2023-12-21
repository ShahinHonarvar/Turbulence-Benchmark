
def filter_chars(string):
    char_list = list(string)
    filtered_list = []
    
    for i in range(86, 93):
        if char_list[i] > 'E' and char_list[i] < '~':
            char_list = [c for c in char_list if c != char_list[i]]
    
    return ''.join(char_list)
