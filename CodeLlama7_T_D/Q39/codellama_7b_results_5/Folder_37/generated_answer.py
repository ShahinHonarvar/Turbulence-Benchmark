
def return_n_greatest_chars(my_string):
    # Convert the string to a list of characters
    my_list = list(my_string)
    # Create an empty list to store the sorted characters
    sorted_list = []
    # Loop through each character in the list
    for char in my_list:
        # If the character is not already in the sorted list, add it
        if char not in sorted_list:
            sorted_list.append(char)
    # Sort the list of characters in descending order by their ASCII values
    sorted_list.sort(key=ord, reverse=True)
    # Return the top 26 characters from the sorted list
    return sorted_list[:26]
