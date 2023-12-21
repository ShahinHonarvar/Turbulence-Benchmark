
def filter_chars(string):
    # Initialize an empty string to store the filtered characters
    filtered_string = ""

    # Iterate over each character in the given string
    for char in string:
        # Check if the current character is between indices 83 and 99, both inclusive
        if 83 <= ord(char) <= 99:
            # Check if the current character is greater than or equal to '*' and smaller than or equal to 'j'
            if char >= "*" and char <= "j":
                # Skip adding this character to the filtered string
                continue

        # Add the current character to the filtered string
        filtered_string += char

    # Return the filtered string
    return filtered_string
