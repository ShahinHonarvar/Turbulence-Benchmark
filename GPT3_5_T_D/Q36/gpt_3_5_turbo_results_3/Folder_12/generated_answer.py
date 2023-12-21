
def filter_chars(string):
    filtered_string = ''
    
    for i in range(len(string)):
        if 32 < i < 84 and ord(string[i]) > ord('m') and ord(string[i]) < ord('w'):
            continue
        filtered_string += string[i]
    
    return filtered_string
