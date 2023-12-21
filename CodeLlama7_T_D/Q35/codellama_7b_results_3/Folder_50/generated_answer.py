
def remove_repeat_chars(s):
    # Create a dictionary to keep track of character frequencies
    char_freq = {}

    # Iterate over the string and count the frequency of each character
    for c in s:
        if c not in char_freq:
            char_freq[c] = 1
        else:
            char_freq[c] += 1

    # Iterate over the characters in the string and remove any duplicates
    new_s = ""

    for i, c in enumerate(s):
        if char_freq[c] == 1:
            new_s += c

    return new_s
