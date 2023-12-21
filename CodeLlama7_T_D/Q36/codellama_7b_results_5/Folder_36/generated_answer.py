
def filter_chars(string):
    # Create a new string with the same length as the original string
    filtered_string = ""

    # Iterate over each character in the original string
    for char in string:
        # If the current character is greater than 'l' and smaller than 't', remove all occurrences of that character within the filtered string while keeping the order of all characters intact.
        if "l" < char < "t":
            filtered_string = filtered_string.replace(char, "")

    # Return the altered string
    return filtered_string
