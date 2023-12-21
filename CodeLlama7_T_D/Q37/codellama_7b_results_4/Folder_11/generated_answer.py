 def filter_chars(s):
    # Initialize an empty string to store the filtered characters
    filtered = ""

    # Iterate over each character in the given string
    for char in s:

        # Check if the current character is between indices 29 and 97, both inclusive, and is greater than or equal to character '-' and smaller than or equal to character 'n'
        if 29 <= ord(char) <= 97 and char >= "-" and char <= "n":

            # If the current character meets the criteria, do not include it in the filtered string
            continue


        # Otherwise, include the current character in the filtered string
        filtered += char

    # Return the filtered string
    return filtered
