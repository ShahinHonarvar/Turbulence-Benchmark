
def remove_repeat_chars(s):
    # Create a dictionary to keep track of character frequencies
    char_freq = {}
    for i in range(len(s)):
        if s[i] not in char_freq:
            char_freq[s[i]] = 1
        else:
            char_freq[s[i]] += 1
    # Remove characters that occur more than once between indices 50 and 92, exclusive
    for i in range(50, len(s)):
        if char_freq[s[i]] > 1:
            s = s[:i] + s[i+1:]
    return s
