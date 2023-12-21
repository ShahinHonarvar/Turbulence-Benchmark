 def filter_chars(s):
    # Initialize an empty list to store the filtered characters
    filtered = []

    # Iterate over the characters in the input string
    for char in s:
        # Check if the current character is between indices 51 and 77, both inclusive
        if (char.isalpha() and char.islower()) and (51 <= ord(char) <= 77):
            # If it is, check if it meets the additional conditions of being greater than or equal to character 'V' and smaller than or equal to character 'Y'
            if char >= "V" and char <= "Y":
                # If both conditions are met, remove all occurrences of this character from the input string
                filtered.append(char)

    # Return the altered string with all characters between indices 51 and 77, both inclusive, removed if they meet the additional condition of being greater than or equal to character 'V' and smaller than or equal to character 'Y', while preserving the order of all characters in the input string.
    return "".join(filtered)
