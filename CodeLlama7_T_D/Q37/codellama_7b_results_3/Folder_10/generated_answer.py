 def filter_chars(s):
    # Create a set of all characters in the given string
    char_set = set(s)
    # Iterate over each character in the string
    for char in s:
        # Check if the current character is between indices 63 and 84, both inclusive
        if (char_set.index(char) >= 63) & (char_set.index(char) <= 84):
            # If the current character is in this range, check if it meets the other criteria
            if (char >= 'E') & (char <= '~'):
                # If the current character meets both criteria, remove all occurrences of that character from the string
                s = s.replace(char, "")
    return s
