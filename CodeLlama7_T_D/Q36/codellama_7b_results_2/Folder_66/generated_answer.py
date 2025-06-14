
def filter_chars(s):
    # Create a new string with the same length as the original string
    result = ""

    # Iterate over each character in the original string
    for c in s:

        # If the current character is between the indices 39 and 87 (both exclusive) and it is greater than character '!' and smaller than character '}', remove all occurrences of that character within the string while keeping the order of all characters in the string intact.
        if (c > 38 and c < 88) and (c > "!" and c < "}"):
            result = result.replace(c, "")

        # If the current character is not between the indices 39 and 87 (both exclusive) or it is not greater than character '!' or it is not smaller than character '}', append the current character to the new string.
        else:
            result += c

    # Return the altered string
    return result
