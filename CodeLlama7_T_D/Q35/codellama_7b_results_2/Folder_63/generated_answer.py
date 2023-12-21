
def remove_repeat_chars(s):
    # Initialize a dictionary to keep track of character frequencies
    freq = {}

    # Iterate over the characters in the given string
    for char in s:
        # If the current character has already been seen, increment its frequency count
        if char in freq:
            freq[char] += 1
        # Otherwise, set the frequency count to 1
        else:
            freq[char] = 1

    # Initialize a new string to store the altered input
    new_s = ""

    # Iterate over the characters in the given string
    for char in s:
        # If the current character has not been seen before, append it to the new string
        if freq[char] == 1:
            new_s += char

        # Otherwise, do not append the current character to the new string
        else:
            pass


    # Return the altered input string with all repeated characters removed
    return new_s
