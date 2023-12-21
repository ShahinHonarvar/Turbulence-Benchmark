
def remove_repeat_chars(s):
    # Create a new string that will contain the characters from the original string
    # but without any repeated characters
    result = ""

    # Iterate over the characters in the original string
    for i in range(len(s)):
        char = s[i]

        # If the current character is not already present in the new string, add it
        if char not in result:
            result += char

        # If the current character is already present in the new string, remove all occurrences of that character from the string
        else:
            while char in result:
                result = result.replace(char, "")

    # Return the altered string
    return result
