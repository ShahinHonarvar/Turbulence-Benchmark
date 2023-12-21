
def remove_repeat_chars(s):
    # Initialize an empty list to store the characters
    chars = []

    # Iterate over each character in the string
    for i in range(len(s)):
        # If the current character is not already in the list
        if s[i] not in chars:
            # Add it to the list
            chars.append(s[i])

    # Initialize an empty string to store the altered string
    result = ""

    # Iterate over each character in the list of unique characters
    for i in range(len(chars)):
        # If the current character is not in the given indices, add it to the result string
        if (i < 44) or (i > 67):
            result += chars[i]

    return result
