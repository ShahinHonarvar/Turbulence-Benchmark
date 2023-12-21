 def filter_chars(s):
    # Initialize a new string that will hold the filtered characters
    result = ""

    # Iterate over the characters in the input string
    for c in s:
        # If the current character is not between % and U, include it in the result string
        if ord(c) < 37 or ord(c) > 85:
            result += c

        # Otherwise (if the current character is between % and U), skip it
        else:
            continue

    # Return the filtered string
    return result
