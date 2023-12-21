
def remove_repeat_chars(s):
    # Create a dictionary to keep track of character counts
    char_counts = {}

    # Iterate over the characters in the string
    for char in s:

        # If the character is already in the dictionary, increment its count
        if char in char_counts:
            char_counts[char] += 1

        # Otherwise, add it to the dictionary with a count of 1
        else:
            char_counts[char] = 1

    # Iterate over the characters in the string again
    for char in s:

        # If the character has a count greater than 1, remove all instances of that character from the string
        if char_counts[char] > 1:
            s = s.replace(char, '')

    # Return the altered string
    return s
