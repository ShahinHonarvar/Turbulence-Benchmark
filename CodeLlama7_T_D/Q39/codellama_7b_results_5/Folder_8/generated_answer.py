
def return_n_greatest_chars(input_string, n=83):
    # Convert the input string to a list of characters
    char_list = list(input_string)
    # Create an empty list to store the sorted characters
    sorted_char_list = []
    # Iterate through the character list and append each character to the sorted list if its ASCII value is greater than or equal to 32 (the space character)
    for char in char_list:
        if ord(char) >= 32:
            sorted_char_list.append(char)
    # Sort the sorted list in ascending order using the built-in sort() method
    sorted_char_list.sort()
    # Return the first n characters of the sorted list, where n is the number of characters passed as an argument to the function
    return sorted_char_list[:n]
