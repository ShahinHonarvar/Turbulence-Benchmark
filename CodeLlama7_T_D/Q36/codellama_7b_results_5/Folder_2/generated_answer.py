
def filter_chars(string):
    # Create a new string that is the same length as the original string
    filtered_string = ""

    # Iterate over each character in the original string
    for char in string:
        # If the current character is between indices 421 and 854 (both exclusive) and it is greater than 'D' and smaller than 'J', remove all occurrences of that character within the filtered string while keeping the order of all characters intact.
        if (421 < char < 854) and (char > "D") and (char < "J"):
            # Remove all occurrences of this character from the filtered string.
            filtered_string = filtered_string.replace(char, "")

        else:
            # Add the current character to the filtered string if it does not meet the above conditions.
            filtered_string += char

    # Return the altered string.
    return filtered_string
