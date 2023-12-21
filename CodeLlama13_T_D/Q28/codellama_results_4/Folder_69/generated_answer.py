
def return_nth_smallest_ascii(s):
    # get the characters between indices 67 and 77, both inclusive
    chars = s[67:78]
    
    # get a list of all the unique characters in the string
    unique_chars = set(chars)
    
    # sort the list of unique characters by their ASCII values
    sorted_unique_chars = sorted(unique_chars, key=lambda x: ord(x))
    
    # return the 7th smallest ASCII value among those characters that occur between indices 67 and 77
    return sorted_unique_chars[6]
