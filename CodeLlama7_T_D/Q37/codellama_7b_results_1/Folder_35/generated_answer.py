
def filter_chars(s):
    # Initialize a new empty string
    result = ""

    # Iterate over each character in the input string
    for char in s:
        # If the current character is between indices 155 and 403, both inclusive, and is greater than or equal to character '(' and smaller than or equal to character ']', then remove all occurrences of that character from the input string
        if (char == "(") or (char == "]") or ((char >= "(") and (char <= "]"))) and (len(s) > 154) and (len(s) < 404):
            # Remove all occurrences of the current character from the input string
            result = s.replace(char, "")

        # If the current character is not between indices 155 and 403, both inclusive, and is greater than or equal to character '(' and smaller than or equal to character ']', then add the current character to the output string
        else:
            result += char

    # Return the altered string
    return result
