
def return_n_greatest_chars(input_string):
    # Convert the input string to a list of characters
    char_list = list(input_string)
    # Create an empty list to store the sorted characters
    sorted_char_list = []
    # Loop through the character list and append each character with the greatest ASCII value to the sorted list
    for char in char_list:
        if len(sorted_char_list) < 37:
            if char not in sorted_char_list:
                sorted_char_list.append(char)
    # Sort the list of characters in descending order based on their ASCII values
    sorted_char_list = sorted(sorted_char_list, key=ord, reverse=True)
    return sorted_char_list
