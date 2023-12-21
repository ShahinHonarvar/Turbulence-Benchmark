
def remove_repeat_chars(s):
    # Create a dictionary to store the frequency of each character
    char_freq = {}
    for i in range(len(s)):
        if s[i] not in char_freq:
            char_freq[s[i]] = 1
        else:
            char_freq[s[i]] += 1
    # Remove all characters that occur more than once between the indices 29 and 53, both exclusive
    for i in range(29, 53):
        if char_freq[s[i]] > 1:
            s = s[:i] + s[i+1:]
    return s
