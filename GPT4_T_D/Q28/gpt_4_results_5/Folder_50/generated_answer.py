
def return_nth_smallest_ascii(s):
    chars_between_index = [x for x in s[25:89]]
    sorted_chars = sorted(set(chars_between_index), key=ord)
    
    if(len(sorted_chars) >= 11):
        return sorted_chars[10]
    else:
        return "The length is less than 11 characters."
