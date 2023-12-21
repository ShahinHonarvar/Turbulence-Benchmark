
def remove_repeat_chars(s):
    # Create a dictionary to keep track of the characters and their counts
    char_counts = {}

    # Iterate over the characters in the given string
    for c in s:

        # If the character is already in the dictionary, increment its count
        if c in char_counts:
            char_counts[c] += 1

        # Otherwise, add the character to the dictionary with a count of 1
        else:
            char_counts[c] = 1

    # Iterate over the characters in the string again, this time removing any characters that have a count greater than 1
    for i, c in enumerate(s):
        if char_counts[c] > 1:
            s = s[:i] + s[i+1:]

    # Return the altered string
    return s
