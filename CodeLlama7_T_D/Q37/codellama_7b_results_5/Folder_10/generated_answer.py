
def filter_chars(s):
    # Create a new empty string
    result = ""

    # Iterate over the characters of the input string
    for char in s:
        # If the character is between indices 63 and 84, both inclusive, and is greater than or equal to character 'E' and smaller than or equal to character '~', then append it to the result string
        if 63 <= ord(char) <= 84 and char >= "E" and char <= "~":
            result += char

    # Return the altered string
    return result
