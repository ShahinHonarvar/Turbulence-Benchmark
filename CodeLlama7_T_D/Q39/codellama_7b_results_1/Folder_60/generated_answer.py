
def return_n_greatest_chars(my_string, n):
    # Sort the characters of the string in descending order based on their ASCII values
    sorted_list = sorted(my_string, key=ord, reverse=True)
    # Return the top 28 characters of the sorted list
    return sorted_list[:n]
