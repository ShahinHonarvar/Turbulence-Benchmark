
def filter_chars(s):
    # Create a new string with the same length as the original string
    result = ""

    # Iterate over each character in the original string
    for i in range(len(s)):

        # Check if the current character is between 70 and 74 (exclusive)
        if ord(s[i]) >= 70 and ord(s[i]) < 75:

            # If it is, remove all occurrences of that character within the string while keeping the order of all characters intact
            result = result + s[i:]
            break

        else:

            # Otherwise, add the current character to the new string
            result = result + s[i]

    return result
