
def filter_chars(s):
    # Create a new string with the same length as the input string
    result = "" * len(s)
    # Iterate over each character in the input string
    for i, c in enumerate(s):
        # If the current character is between indices 26 and 64, both inclusive
        if 26 <= i <= 64:
            # And it is greater than or equal to character 'V' and smaller than or equal to character 'o', both inclusive
            if c >= "V" and c <= "o":
                # Then remove all occurrences of that character from the result string
                result = result.replace(c, "")
        # Otherwise, just append the current character to the result string
        else:
            result += c

    return result
