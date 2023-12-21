
def return_n_greatest_chars(my_string):
    # Sort the characters in the string by their ASCII values
    sorted_chars = sorted(my_string, key=ord)
    # Return the top 47 characters of the sorted list
    return sorted_chars[:47]
