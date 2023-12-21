
def remove_repeat_chars(input_string):
    # Create a list of characters from the input string
    char_list = list(input_string)
    # Initialize a variable to keep track of the number of characters removed
    num_removed = 0
    # Iterate through the characters in the list
    for i in range(len(char_list)):
        # If the current character is repeated between the indices 57 and 85, exclusive
        if char_list[i] in input_string[57:85]:
            # Remove all occurrences of the current character from the string
            char_list = [char for char in char_list if char != char_list[i]]
            # Increment the number of characters removed by 1
            num_removed += 1
    # Join the list of characters back into a string and return it
    return "".join(char_list)
