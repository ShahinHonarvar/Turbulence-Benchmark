
def filter_chars(my_string):
    # Create a new string with all characters removed
    filtered_string = ""

    # Iterate over each character in the given string
    for char in my_string:

        # Check if the current character is between indices 259 and 502, both inclusive
        if 259 <= ord(char) <= 502:

            # Check if the current character is greater than or equal to ',' and smaller than or equal to '3'
            if char >= ',' and char <= '3':

                # Skip this character since it meets the criteria
                continue


        # Add the current character to the filtered string
        filtered_string += char

    # Return the altered string
    return filtered_string
