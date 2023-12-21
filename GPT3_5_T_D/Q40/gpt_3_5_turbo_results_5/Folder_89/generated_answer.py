

def return_n_smallest_chars(string):
    # Create a list of characters by converting the string to a list
    chars = list(string)
    
    # Sort the list of characters in ascending order of ASCII values
    sorted_chars = sorted(chars)
    
    # Return the first 55 characters from the sorted list
    return sorted_chars[:55]
