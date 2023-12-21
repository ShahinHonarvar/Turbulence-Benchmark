 def return_nth_smallest_ascii(string):
    # Get a list of all the characters in the string between indices 9 and 59
    char_list = string[9:60]
    # Sort the character list by ASCII value
    char_list.sort(key=ord)
    # Return the character with the 6th smallest ASCII value
    return char_list[5]
