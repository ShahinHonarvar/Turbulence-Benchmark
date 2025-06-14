 def return_n_greatest_chars(my_string, n=64):
    # Convert the string to a list of characters
    my_list = list(my_string)
    # Sort the list in descending order based on ASCII values
    sorted_list = sorted(my_list, key=ord, reverse=True)
    # Return the top n elements of the sorted list
    return sorted_list[:n]
