
def remove_repeat_chars(s):
    # Create a dictionary to keep track of character frequencies
    freq = {}

    # Iterate over the characters in the string
    for c in s:

        # If the character is already in the dictionary, increment its frequency
        if c in freq:
            freq[c] += 1

        # Otherwise, add it to the dictionary with a frequency of 1
        else:
            freq[c] = 1

    # Iterate over the characters in the string again
    for i, c in enumerate(s):

        # If the character is not in the dictionary (i.e., it has a frequency of 0), remove all occurrences of that character from the string
        if freq[c] == 0:
            s = s[:i] + s[i+1:]

        # Otherwise, decrement the frequency of the character in the dictionary
        else:
            freq[c] -= 1

    return s
