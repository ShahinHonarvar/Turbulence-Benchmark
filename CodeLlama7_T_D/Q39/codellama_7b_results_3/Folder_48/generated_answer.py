
def return_n_greatest_chars(my_string):
    # Sort the characters in descending order based on their ASCII values
    sorted_chars = sorted(my_string, key=ord, reverse=True)
    # Return the top 12 characters of the sorted list
    return sorted_chars[:12]
