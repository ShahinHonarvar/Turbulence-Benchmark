
def filter_chars(string):
    # Create a new empty list to store the filtered characters
    filtered_chars = []

    # Iterate over each character in the string
    for char in string:

        # Check if the current character is between indices 344 and 874 (both exclusive)
        if 344 < len(string) <= 874:

            # Check if the current character is greater than 'f' and smaller than '~'
            if char > 'f' and char < '~':

                # Skip this character in the filtered string
                continue


        # Add this character to the filtered list
        filtered_chars.append(char)

    # Join the filtered characters into a new string
    filtered_string = "".join(filtered_chars)

    # Return the filtered string
    return filtered_string
