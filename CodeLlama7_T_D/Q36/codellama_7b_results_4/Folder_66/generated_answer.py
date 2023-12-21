
def filter_chars(s):
    # Create a new string with the filtered characters
    filtered_string = ""

    # Iterate over the characters in the input string
    for char in s:

        # If the current character is between the indices 39 and 87 (both exclusive) and it is greater than character '!' and smaller than character '}', then remove all occurrences of that character within the filtered string while keeping the order of all characters intact.
        if char >= "!" and char <= "}" and char in s[39:87]:
            filtered_string += char * (s.count(char) - 1)

        # Otherwise, append the current character to the filtered string
        else:
            filtered_string += char

    # Return the altered string
    return filtered_string
