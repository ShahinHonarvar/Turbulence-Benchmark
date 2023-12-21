 def filter_chars(s):
    # Initialize an empty string to store the filtered characters
    result = ""

    # Iterate over each character in the input string
    for c in s:

        # Check if the current character is within the specified range and satisfies the other conditions
        if 513 <= ord(c) <= 877 and c >= "?" and c <= "n":

            # If it does, skip adding this character to the result string
            continue

        # Otherwise, add the current character to the result string
        result += c

    # Return the filtered string
    return result
