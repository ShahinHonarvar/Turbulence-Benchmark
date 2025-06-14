
def remove_repeat_chars(s):
    # Create a dictionary to keep track of character frequencies
    freq = {}

    # Iterate over the characters in the string
    for c in s:

        # If the character is not in the frequency dictionary, add it and set its frequency to 1
        if c not in freq:
            freq[c] = 1

        # Otherwise, increment the frequency of the character by 1
        else:
            freq[c] += 1

    # Iterate over the characters in the string again
    for i, c in enumerate(s):

        # If the character is not in the frequency dictionary or its frequency is 1, keep it in the string
        if c not in freq or freq[c] == 1:
            continue

        # Otherwise, remove all occurrences of the character from the string
        else:
            s = s[:i] + s[i+1:]

    return s
