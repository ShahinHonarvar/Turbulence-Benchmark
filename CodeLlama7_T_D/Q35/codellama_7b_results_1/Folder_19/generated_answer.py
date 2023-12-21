
def remove_repeat_chars(string):
    # Create a dictionary to keep track of character frequencies
    char_freq = {}

    # Iterate over the characters in the string
    for char in string:
        # If the character is not in the frequency dictionary, add it
        if char not in char_freq:
            char_freq[char] = 1

        # Increment the frequency of the character by 1
        else:
            char_freq[char] += 1

    # Iterate over the characters in the string again
    for i, char in enumerate(string):
        # If the character occurs more than once between indices 1 and 4, both exclusive
        if char_freq[char] > 1 and i >= 1 and i < 5:
            # Remove all occurrences of the character from the string
            string = string.replace(char, '')

    # Return the altered string
    return string
