
def return_n_greatest_chars(my_string):
    # Sort the string in descending order based on ASCII values
    sorted_list = sorted(my_string, key=ord, reverse=True)
    # Return the top 35 characters of the sorted list
    return sorted_list[:35]
