
def remove_repeat_chars(input_string):
    # Initialize an empty list to store the characters of the input string
    character_list = []

    # Iterate over each character in the input string
    for char in input_string:

        # If the current character is not already in the character_list, append it to the list
        if char not in character_list:
            character_list.append(char)

    # Initialize an empty string to store the characters of the input string that are not repeated
    output_string = ""

    # Iterate over each character in the character_list
    for char in character_list:

        # If the current character is not repeated between the indices 56 and 90, exclusive, append it to the output string
        if input_string.count(char) == 1 or (input_string.index(char) >= 56 and input_string.index(char) < 90)):
            output_string += char

    return output_string
