
def return_nth_smallest_ascii(s):
    if len(s) < 77:
        return "Invalid input - string length is less than 76."
    
    char_list = sorted(s[50:77], key=ord)
    if len(char_list) < 11:
        return "Not enough distinct characters in the range specified."
    
    return char_list[10]
