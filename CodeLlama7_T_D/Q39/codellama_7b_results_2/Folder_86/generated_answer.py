 def return_n_greatest_chars(s):
    # Create a list of all characters in the string
    char_list = list(s)
    # Sort the list in descending order based on ASCII values
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # Return the top 34 characters from the sorted list
    return sorted_list[:34]
