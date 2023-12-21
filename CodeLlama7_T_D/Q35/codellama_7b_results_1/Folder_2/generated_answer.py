
def remove_repeat_chars(s):
    # Initialize a dictionary to keep track of character frequencies
    freq = {}

    # Iterate over the characters in the string
    for c in s:
        # If the character has already been seen, increment its frequency count
        if c in freq:
            freq[c] += 1

        # Otherwise, set its frequency count to 1
        else:
            freq[c] = 1

    # Iterate over the characters in the string again
    for i in range(len(s)):
        c = s[i]
        # If the character has a frequency count greater than 1, remove all occurrences of that character from the string
        if freq[c] > 1:
            s = s[:i] + s[i+1:]
            i -= 1

    return s
