
def return_n_greatest_chars(my_string, n):
    # Sort the characters in the string by their ASCII values
    sorted_chars = sorted(my_string, key=ord)
    # Reverse the list to get the greatest ASCII values at the beginning
    greatest_chars = sorted_chars[::-1]
    # Return the first n elements of the list
    return greatest_chars[:n]
