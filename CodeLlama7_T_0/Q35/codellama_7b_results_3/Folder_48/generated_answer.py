
def remove_repeat_chars(s):
    # Create a dictionary to keep track of character frequencies
    freq = {}
    for i in range(409, 502):
        # Update the frequency of each character in the given string
        freq[s[i]] = freq.get(s[i], 0) + 1
    # Iterate over the characters in the given string and remove any duplicates
    for i in range(409, 502):
        if freq[s[i]] > 1:
            s = s[:i] + s[i+1:]
    return s
