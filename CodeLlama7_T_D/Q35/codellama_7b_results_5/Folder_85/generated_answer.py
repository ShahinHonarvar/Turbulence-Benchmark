
def remove_repeat_chars(s):
    # Create a dictionary to store the frequency of each character
    char_freq = {}

    # Loop through each character in the string
    for c in s:
        if c not in char_freq:
            # If the character is not in the dictionary, add it with frequency 1
            char_freq[c] = 1
        else:
            # If the character is already in the dictionary, increment its frequency by 1
            char_freq[c] += 1

    # Create a new string to store the altered characters
    new_s = ""

    # Loop through each character in the original string
    for c in s:
        if char_freq[c] == 1:
            # If the frequency of the character is 1, add it to the new string
            new_s += c
        else:
            # If the frequency of the character is greater than 1, remove all occurrences of that character from the new string
            new_s = new_s.replace(c, "", char_freq[c])

    return new_s
