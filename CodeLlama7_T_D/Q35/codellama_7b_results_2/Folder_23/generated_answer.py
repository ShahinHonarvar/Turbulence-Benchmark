 def remove_repeat_chars(s):
    # Create a new string with the characters removed
    new_string = ""

    # Iterate through each character in the given string
    for char in s:

        # If the current character is not repeated between indices 20 and 36, inclusive
        if not (char in s[20:36]):
            new_string += char

        # If the current character is repeated more than once between indices 20 and 36, exclusive
        else:
            # Get the indices of all occurrences of the current character in the given string
            indices = [i for i, ltr in enumerate(s) if ltr == char]

            # If there are no repeated characters in the given string between indices 20 and 36, exclusive
            if not indices:
                new_string += char

            # If there are repeated characters in the given string between indices 20 and 36, exclusive
            else:
                # Get the last index of all occurrences of the current character in the given string
                last_index = max(indices)

                # If the last index of the current character is less than or equal to the index 36
                if last_index <= 36:
                    new_string += char

                # If the last index of the current character is greater than the index 36
                else:
                    continue

    return new_string
