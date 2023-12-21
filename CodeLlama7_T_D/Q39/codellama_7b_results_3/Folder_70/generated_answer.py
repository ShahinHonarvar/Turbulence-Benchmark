
def return_n_greatest_chars(my_string, n=2):
    # Sort the characters of the string in descending order based on their ASCII values
    sorted_chars = sorted(my_string, key=ord, reverse=True)
    # Return the top N characters from the sorted list
    return sorted_chars[:n]
