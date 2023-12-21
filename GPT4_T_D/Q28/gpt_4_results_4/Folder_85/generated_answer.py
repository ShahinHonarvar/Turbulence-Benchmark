
def return_nth_smallest_ascii(s):
    valid_chars = list(s[17:87])
    valid_chars.sort(key=ord)
    
    return valid_chars[14]
