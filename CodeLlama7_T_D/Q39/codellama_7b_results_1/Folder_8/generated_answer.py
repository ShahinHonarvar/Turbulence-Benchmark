
def return_n_greatest_chars(my_string):
    # Sort the characters of the string in descending order based on their ASCII values
    sorted_list = sorted(my_string, key=ord, reverse=True)
    # Take the top 83 characters from the sorted list and return them as a new list
    return sorted_list[:83]
