
def filter_chars(string):
    # Initialize an empty string for the filtered characters
    filtered_string = ""

    # Iterate over each character in the original string
    for char in string:
        # If the current character is between indices 71 and 94, both inclusive,
        if 71 <= ord(char) <= 94:
            # And it is greater than or equal to 'K' and smaller than or equal to 'a', both inclusive,
            if char >= "K" and char <= "a":
                # Then skip this character in the filtered string
                continue

        # Otherwise, add the current character to the filtered string
        filtered_string += char

    # Return the filtered string
    return filtered_string
