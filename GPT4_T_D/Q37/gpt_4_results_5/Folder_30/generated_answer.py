
def filter_chars(input_string):
    to_remove = set(input_string[41:65]).intersection(set(ch for ch in range(ord('K'), ord(']')+1)))
    
    return ''.join(ch for ch in input_string if ch not in to_remove)
