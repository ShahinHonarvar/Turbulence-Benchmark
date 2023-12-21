
def return_nth_smallest_ascii(string):
    # Get the characters between indices 3 and 52, both inclusive
    char_list = string[3:52]
    
    # Create a list of tuples containing each character and its ASCII value
    char_value_pairs = [(char, ord(char)) for char in char_list]
    
    # Sort the list by the second element (ASCII value)
    sorted_pairs = sorted(char_value_pairs, key=lambda x: x[1])
    
    # Return the 8th character from the sorted list
    return sorted_pairs[7][0]
