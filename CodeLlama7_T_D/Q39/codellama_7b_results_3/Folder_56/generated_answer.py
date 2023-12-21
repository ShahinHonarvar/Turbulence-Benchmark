
def return_n_greatest_chars(my_string):
    # Sort the characters in the string based on their ASCII values
    sorted_list = sorted(my_string, key=ord)
    # Return the top 21 characters of the sorted list
    return sorted_list[:21]
