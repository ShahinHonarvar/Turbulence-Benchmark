
def filter_chars(s):
    # Initialize an empty string to store the filtered characters
    filtered = ""

    # Iterate through each character in the given string
    for char in s:
        # Check if the current character is between indices 259 and 502, both inclusive, and is greater than or equal to character ',' and smaller than or equal to character '3'
        if (259 <= s.index(char)) and (s.index(char) <= 502) and ("," <= char) and (char <= "3"):
            # If the current character meets the condition, skip it
            continue

        # Otherwise, append the current character to the filtered string
        filtered += char

    # Return the altered string with the filtered characters removed
    return filtered
