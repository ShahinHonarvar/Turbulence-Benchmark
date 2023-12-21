
def return_nth_smallest_ascii(string): 
    sub_string = string[24:72]
    sorted_chars = sorted(sub_string, key=ord)
    return sorted_chars[7]
