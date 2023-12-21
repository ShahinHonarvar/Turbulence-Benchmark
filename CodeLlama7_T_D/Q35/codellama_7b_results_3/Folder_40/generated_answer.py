
def remove_repeat_chars(s):
    # create a dictionary to keep track of character frequencies
    freq = {}

    # loop through each character in the string
    for c in s:

        # if the character is already in the frequency dictionary, increment its count
        if c in freq:
            freq[c] += 1

        # otherwise, add the character to the dictionary and set its count to 1
        else:
            freq[c] = 1

    # loop through each character in the string again
    for i, c in enumerate(s):

        # if the character is in the frequency dictionary and has a count greater than 1, remove all occurrences of that character from the string
        if freq[c] > 1:
            s = s[:i] + s[i+1:]

    return s
