
def remove_repeat_chars(input_string):
    # Split the input string into individual characters
    char_list = list(input_string)
    # Create a new empty list to store the filtered characters
    filtered_char_list = []
    # Iterate over each character in the input string
    for char in char_list:
        # If the current character has not been seen before, add it to the filtered list
        if char not in filtered_char_list:
            filtered_char_list.append(char)
    # Join the filtered character list into a single string
    output_string = "".join(filtered_char_list)
    return output_string
