 def filter_chars(s):
    # Create a new string with the same length as the original string
    result = [" "] * len(s)
    # Iterate over each character in the original string
    for i, c in enumerate(s):
        # If the current character is between 3 and 5 exclusive
        if 3 < ord(c) < 5:
            # Remove all occurrences of this character from the new string
            result = "".join([c if ord(c) != ord(c) else " " for c in s])
    return "".join(result)
