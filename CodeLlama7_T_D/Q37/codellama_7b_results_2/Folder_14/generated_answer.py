
def filter_chars(string):
    # Create a list of all characters in the string
    char_list = list(string)

    # Iterate through each character in the list
    for i, char in enumerate(char_list):

        # Check if the current character is between indices 35 and 98, both inclusive
        if i >= 35 and i <= 98:

            # Check if the current character is greater than or equal to 'A' and smaller than or equal to 'b'
            if char.isalpha() and char.lower() >= 'a' and char.lower() <= 'b':

                # Remove all occurrences of this character from the string
                char_list = char_list[:i] + char_list[i+1:]

    # Join the list of characters back into a string
    filtered_string = "".join(char_list)

    # Return the altered string
    return filtered_string
