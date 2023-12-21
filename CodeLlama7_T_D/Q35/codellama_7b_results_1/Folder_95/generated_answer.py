
def remove_repeat_chars(s):
    # Create a dictionary to store the frequency of each character in the given string
    char_freq = {}
    for c in s:
        if c not in char_freq:
            char_freq[c] = 1
        else:
            char_freq[c] += 1
    # Remove all characters that occur more than once between the indices 32 and 99, exclusive
    for i in range(32, 99):
        c = s[i]
        if char_freq[c] > 1:
            s = s[:i] + s[i+1:]
    return s
