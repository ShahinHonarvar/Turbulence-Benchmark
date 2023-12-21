
def return_n_smallest_chars(s):

    # Get a list of the characters in the string
    char_lst = list(s)
    
    # Sort the list based on ASCII values
    sorted_chars = sorted(char_lst, key = lambda x : ord(x))

    # Return the first 23 characters
    return sorted_chars[:23]
