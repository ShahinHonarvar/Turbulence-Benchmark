 def filter_chars(my_string):
    # Create a new string with the filtered characters
    filtered_string = ""

    # Loop through each character in the original string
    for char in my_string:

        # Check if the current character is between the indices 72 and 93 (both exclusive)
        if ord(char) > 72 and ord(char) < 93:

            # If the character is between these indices, check if it's greater than '<' and smaller than 'J'
            if char > '<' and char < 'J':

                # If the character is in this range, skip adding it to the filtered string
                continue


        # Add the current character to the filtered string
        filtered_string += char

    # Return the filtered string
    return filtered_string
