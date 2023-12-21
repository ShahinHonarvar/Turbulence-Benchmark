
def remove_repeat_chars(input_string):
    # Split the input string into individual characters
    char_list = list(input_string)
    # Create a new list to store the output string
    output_list = []
    # Iterate through each character in the input string
    for char in char_list:
        # If the current character is not already in the output list, add it
        if char not in output_list:
            output_list.append(char)
    # Join the elements of the output list into a single string
    output_string = "".join(output_list)
    return output_string
