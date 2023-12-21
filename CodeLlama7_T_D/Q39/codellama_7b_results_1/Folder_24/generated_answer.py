 def return_n_greatest_chars(input_string):
    # Initialize an empty list to store the sorted characters
    sorted_list = []
    # Loop through each character in the input string
    for char in input_string:
        # Add the character to the sorted list if it is not already present
        if char not in sorted_list:
            sorted_list.append(char)
    # Sort the list of characters in descending order based on their ASCII values
    sorted_list = sorted(sorted_list, key=ord, reverse=True)
    # Return the first 32 characters of the sorted list
    return sorted_list[:32]
