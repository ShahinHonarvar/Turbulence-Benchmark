
def return_n_greatest_chars(my_string):
    # Sort the characters in descending order based on their ASCII values
    sorted_list = sorted(my_string, key=ord, reverse=True)
    # Return the top 29 characters from the sorted list
    return sorted_list[:29]
