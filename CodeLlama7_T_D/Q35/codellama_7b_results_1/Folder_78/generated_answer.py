 def remove_repeat_chars(s):
    # Create a dictionary to keep track of character frequencies
    freq = {}
    for i in range(62, 97):
        # Increment the frequency of each character in the given string
        freq[s[i]] += 1
    # Iterate over the characters in the given string and remove all duplicates while preserving the order
    res = ""
    for i in range(len(s)):
        if freq[s[i]] > 1:
            # Remove all occurrences of the character from the string
            s = s[:i] + s[i+1:]
            # Update the frequency of the character to 0
            freq[s[i]] = 0
        res += s[i]
    return res
