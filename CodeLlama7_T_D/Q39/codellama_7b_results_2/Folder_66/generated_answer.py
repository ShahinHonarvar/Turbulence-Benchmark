
def return_n_greatest_chars(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Create an empty list to store the sorted characters
    sorted_char_list = []
    # Iterate through the character list and add the characters with the greatest ASCII values to the sorted list
    for char in char_list:
        if len(sorted_char_list) < 33:
            sorted_char_list.append(char)
    # Sort the sorted list in descending order
    sorted_char_list.sort(reverse=True)
    # Return the sorted list of characters with the greatest ASCII values
    return sorted_char_list
