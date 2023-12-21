
def filter_chars(my_string):
    # Create a new empty list to store the filtered characters
    filtered_characters = []

    # Loop through each character in the given string
    for character in my_string:

        # Check if the current character is between 72 and 93 (both exclusive)
        if ord(character) >= 72 and ord(character) < 93:

            # If the character is greater than '<' and smaller than 'J', skip it
            if character > '<' and character < 'J':
                continue


        # Add the current character to the list of filtered characters
        filtered_characters.append(character)

    # Join all the filtered characters into a single string
    filtered_string = "".join(filtered_characters)

    # Return the altered string
    return filtered_string
