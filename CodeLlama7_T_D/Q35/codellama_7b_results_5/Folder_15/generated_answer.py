
def remove_repeat_chars(s):
    # Create a dictionary to keep track of character frequencies
    char_freq = {}

    # Iterate over the characters in the string
    for c in s:

        # If the character has already been seen, increase its frequency count
        if c in char_freq:
            char_freq[c] += 1

        # Otherwise, set the frequency count to 1
        else:
            char_freq[c] = 1

    # Iterate over the characters in the string again
    for i, c in enumerate(s):

        # If the character has a frequency count greater than 1, remove all instances of that character from the string
        if char_freq[c] > 1:
            s = s[:i] + s[i+1:]

    # Return the altered string
    return s
