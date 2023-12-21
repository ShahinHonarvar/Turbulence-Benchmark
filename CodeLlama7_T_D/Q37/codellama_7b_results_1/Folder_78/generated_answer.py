
def filter_chars(string):
    # Create a new string to store the filtered characters
    filtered_string = ""

    # Iterate through each character in the original string
    for char in string:
        # Check if the current character is between indices 75 and 99, both inclusive
        if 75 <= string.find(char) <= 99:
            # Check if the current character is greater than or equal to character '8' and smaller than or equal to character 'e'
            if char >= "8" and char <= "e":
                # Skip adding this character to the filtered string
                continue

        # If the current character does not meet the criteria, add it to the filtered string
        filtered_string += char

    # Return the filtered string
    return filtered_string
